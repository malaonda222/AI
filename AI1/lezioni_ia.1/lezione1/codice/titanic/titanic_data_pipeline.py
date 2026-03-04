import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import json
from typing import Tuple

class DataSourceConfig:
    """Configurazione sorgenti dati e destinazione output"""
    db_uri: str = "postgresql+psycopg://postgres:postgres@postgresql:5432/titanic_db"
    json_path: str = "../../dati/titanic/titanic_prefs_small.json"
    output_plot: str = "../../visual/titanic/plot.png"

class DataPipeline:
    def __init__(self, config: DataSourceConfig):
        self.config = config
        self.data = None
    
    def load_from_database(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Carica dati da un database PostgreSQL"""
        queries = {
            'passenger': "SELECT * FROM public.passenger_info_small",
            'ticket': "SELECT * FROM public.ticket_info_small"
        }
        
        engine = create_engine(self.config.db_uri)
        try:
            with engine.connect() as conn:
                df1 = pd.read_sql_query(text(queries['passenger']), conn)
                df2 = pd.read_sql_query(text(queries['ticket']), conn)
        except SQLAlchemyError as e:
            print(f"Errore di lettura da database: {e}")
            df1 = pd.DataFrame()
            df2 = pd.DataFrame() 
        finally:
            engine.dispose()
        return df1, df2 
    
    def load_from_json(self) -> pd.DataFrame:
        """Carica dati da un file JSON"""
        return pd.read_json(self.config.json_path)
        
    def merge_data(self, db_df1: pd.DataFrame, db_df2: pd.DataFrame, json_df: pd.DataFrame) -> pd.DataFrame:
        """Aggregazione dati di diverse sorgenti"""
        db_merged = pd.merge(db_df1, db_df2, on='PassengerId') #si crea il primo dataset unendo i due dataframe 
        return pd.merge(db_merged, json_df, on='PassengerId') #
    
    def expand_json_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Parsing ed espansione della colonna JSON di preferenze"""
        df['preferences'] = df['preferences'].apply(json.loads)
        prefs_expanded = pd.json_normalize(df['preferences'])
        return pd.concat([df.drop('preferences', axis=1), prefs_expanded], axis=1)
    
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Operazioni varie di pulizia dati"""        
        
        # Studia il dataframe - Fase pre
        # ESERCIZIO 1 4
        # Task: stampa i tipi del df e le colonne 'Age' ,'Fare', 'Sex' 
        #       delle prime 10 ed ultime 5 righe 
        print(df.dtypes)
        print(df['Age'].head(10))
        print(df['Fare'].head(10)) 
        print(df['Sex'].head(10))

        print(df['Age'].tail(5)) 
        print(df['Fare'].tail(5))
        print(df['Sex'].tail(5))   

        print((df[['Age', 'Fare', 'Sex']]).head(10))
        print([['Age', 'Fare', 'Sex']].tail(5))

        # Sostituisci valori nulli/assenti con NaN
        # ESERCIZIO 2 
        # Task: sostituire i '?' con numpy NaNs   
        print(df.replace("?", np.nan, inplace=True))

        df_clean = df.replace("?", np.nan)

        df_clean = df.replace("?", np.nan)  
        print(df_clean)   
        
        # Limita gli outliers
        # ESERCIZIO 3 
        # Task: stabilisci una soglia max di età ('Age') a cui riportare gli outliers (soglia_max=80)

        df['Age'] = df['Age'].clip(upper=80)

        # Sostituisci NaNs con il valor medio
        # ESERCIZIO 4
        # Task: applicare la sostituzione con il valor medio alle colonne 'Age' e 'Fare'  
     
        df['Age'] = df['Age'].replace(np.nan, df['Age'].mean())
        df['Fare'] = df['Fare'].replace(np.nan, df['Fare'].mean()) 
        #oppure 
        df['Age'] = df['Age'].fillna(df['Age'].mean())
        df['Fare'] = df['Fare'].fillna(df['Fare'].mean())

        # Correzione di errori per contenuti standard
        # ESERCIZIO 6 
        # Task: correggere 'mael' con 'male' e 'femael' con 'female' nella colonna 'Sex'   
        df['Sex'] = df['Sex'].replace({'mael': 'male', 'femael': 'female'})

        # Conversione dei tipi di dato
        # ESERCIZIO 7
        # Task: converti i dati e rendi l'età di tipo float 

        df = df.convert_types()
        df['Age'] = df['Age'].astype("float64")

        # Studia il dataframe - Fase post        
        # ESERCIZIO 8 
        # Task: stampa i tipi del df e le colonne Age' ,'Fare', 'Sex' 
        #       delle prime 10 ed ultime 5 righe, Cosa è cambiato rispetto all'output dell'ESERCIZIO 1?         

        print(df.dtypes)

        print(df['Age'].head(10))
        print(df['Fare'].head(10))
        print(df['Sex'].head(10))

        print(df['Age'].tail(5))
        print(df['Fare'].tail(5))
        print(df['Sex'].tail(5))

        return df
    
    def visualize(self, df: pd.DataFrame) -> None:
        """Crea e salva visualizzazioni"""
    
    def run_pipeline(self) -> pd.DataFrame:
        """Esegue la pipeline completa"""
        # Carica dati
        db_df1, db_df2 = self.load_from_database()       
        print("   -Letti dati da due tabelle su db")
        json_df = self.load_from_json()
        print("   -Letti dati da un file JSON")        
        # Preprocessa dati
        merged_df = self.merge_data(db_df1, db_df2, json_df)
        expanded_df = self.expand_json_data(merged_df)
        print(merged_df.head()) #di default stampa le prime 5 righe 
        print("   -Aggregazione ed espansione dati effettuate")
        clean_df = self.clean_data(expanded_df)
        print("   -Pulizia dati completata")        
        # Visualizza risultati
        self.visualize(clean_df)
        print("   -Analisi e visualizzazione dati terminate")          
        self.data = clean_df
        return clean_df
        
# Uso delle classi
if __name__ == "__main__":
    config = DataSourceConfig() 
    pipeline = DataPipeline(config)
    print("Pipeline avviata...")
    final_df = pipeline.run_pipeline()
    print("Pipeline completata con successo!")
    print(final_df.head())