import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

class DataSourceConfig: #classe che permette di configurare sorgenti dati e destinazione output  
    """Configurazione sorgenti dati e destinazione output"""
    remote_url: str = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
    db_uri: str = "postgresql+psycopg://postgres:postgres@postgresql:5432/auto_db"
    csv_path: str = "../../dati/autos/auto.csv" #percorso di salvataggio del file .csv con dati grezzi
    csv_clean_path: str = "../../dati/autos/auto_clean.csv" #percorso di salvataggio del file .csv con dati puliti
    output_plot: str = "../../visual/autos/plot.png" #percorso di salvataggio del plot dei dati puliti 


class DataPipeline: #classe inizializzata con un'istanza di DataSourceConfig che permette di caricare, pulire, salvare e visualizzare
    def __init__(self, config: DataSourceConfig):
        self.config = config
        self.data = None #per indicare che per ora la sorgente dati non contiene ancora nulla
        
    def load_from_csv(self) -> pd.DataFrame: #carica dati dai un file .csv (se fosse stato dict: pd.DataFrame(dict), se fosse un json: pd.read_json("<nome_file>"))
        """Carica dati da un file CSV"""
        return pd.read_csv(self.config.csv_path)        

    def load_from_remote(self) -> pd.DataFrame: #carica dati da un file remoto + stabilisce nome colonne del dataframe 
        """Carica dati da un file remoto identificato da un URL aggiungendo intestazioni"""
        headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
                  "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
                  "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
                  "peak-rpm","city-mpg","highway-mpg","price"]
        return pd.read_csv(self.config.remote_url, names = headers)
    
    def save_on_csv(self, df: pd.DataFrame) -> None: #salvataggio per dati grezzi in csv dedicato
        """Salva dati in un file CSV"""
        df.to_csv(self.config.csv_path)    
        
    def save_clean_on_csv(self, df: pd.DataFrame) -> None: #salvataggio per dati puliti in csv dedicato
        """Salva dati puliti in un file CSV"""
        df.to_csv(self.config.csv_clean_path)    
    
    def store_on_database(self, df: pd.DataFrame) -> None: #dopo aver pulito i dati, li passiamo al db 
        """Scrive dati in un database PostgreSQL"""      
        table_name = "auto_info"
        engine = create_engine(self.config.db_uri) #apre la connessione, metodo di SQLAlchemy (ponte tra Python e Postgresql)
        try:
            with engine.begin() as conn:  # begin() per gestione automatica di commit/rollback
                df.to_sql(table_name, con=conn, if_exists='replace', index=False)
        except SQLAlchemyError as e:
            print(f"Error di scrittura in database: {e}")
        finally:
            engine.dispose()  # Chiusura pulita e rilascio risorse
        
    def load_from_database(self) -> pd.DataFrame: #contrario rispetto a store, si importano e si caricano i dati dal database 
        """Carica dati da un database PostgreSQL"""
        query_def = "SELECT * FROM public.auto_info"        
        engine = create_engine(self.config.db_uri)
        try:
            with engine.connect() as conn:
                df = pd.read_sql_query(text(query_def), con=conn)
        except SQLAlchemyError as e:
            print(f"Errore di lettura da database: {e}")
            df = pd.DataFrame() 
        finally:
            engine.dispose()  # Chiusura pulita e rilascio risorse
        return df

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Operazioni varie di pulizia dati"""
        df.replace("?", np.nan, inplace=True)
        avg = df["normalized-losses"].astype("float").mean(axis = 0)
        df["normalized-losses"] = df["normalized-losses"].replace(np.nan, avg) #df["normalizes-losses"].replace(np.nan, avg, inplace=True) 
        df["num-of-doors"] = df["num-of-doors"].replace(np.nan, df['num-of-doors'].value_counts().idxmax()) #i due metodi insieme calcolano prima il valore con la frequenza massima e poi sostituisce con il numero con massima frequenza 
        df.dropna(subset=["price"], axis=0, inplace = True) #cancella le righe che hanno na della colonna specificata 
        df.reset_index(drop = True, inplace = True) #resetta l'indice del dataframe 
        df = df.convert_dtypes() #converte in automatico i tipi di dato nel df completo 
        df[["normalized-losses"]] = df[["normalized-losses"]].astype("int") #converte solo una colonna in particolare in int 
        df[["price"]] = df[["price"]].astype("float")
        df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")
        #oppure df[['price', 'peak_rpm']] = df[['price', 'peak_rpm']].astype("float") 
        df['make'] = df['make'].replace({'alfa-romero': 'alfa-romeo', 'peugot': 'peugeot'}) #per modificare, si comporta come un dizionario (chiave: valore da sostituire, valore: nome corretto)
        self.save_clean_on_csv(df) #richiamo metodo di salvataggio per i dati puliti che vengono salvati in self.config.csv_clean_path
        return df 

    def visualize(self, df: pd.DataFrame) -> None:
        """Crea e salva visualizzazioni"""        
        
    def run_pipeline(self) -> pd.DataFrame:
        """Esegue la pipeline completa"""
        # Carica dati da remoto
        remote_df = self.load_from_remote()
        print("   -Letto file remoto")
        # print(remote_df.shape)
        # print(remote_df.head(15))
        # print(remote_df.dtypes)
        # print(remote_df.info())
        # return pd.DataFrame()
        # Salva dati in locale
        self.save_on_csv(remote_df)
        print("   -Salvato file remoto in locale")
        # Scrive dati in database
        self.store_on_database(remote_df)
        print("   -Scritto file remoto in una tabella su db")
        # Legge dati da database
        db_df = self.load_from_database()
        print("   -Letti dati da una tabella su db")
        print(db_df.dtypes)
        # return pd.DataFrame()
        # # Pulizia dati
        clean_df = self.clean_data(db_df)
        print("   -Pulizia dati completata e file pulito salvato")
        # # Visualizza risultati
        self.visualize(clean_df)
        print("   -Analisi e visualizzazione dati terminate")          
        self.data = clean_df
        return clean_df
        
if __name__ == "__main__":
    config = DataSourceConfig()
    pipeline = DataPipeline(config)
    print("Pipeline avviata...")  
    final_df = pipeline.run_pipeline()
    print("Pipeline completata con successo!")
    print(final_df.head())