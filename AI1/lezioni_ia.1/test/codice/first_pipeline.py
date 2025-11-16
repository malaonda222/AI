# pipeline

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

class DataPipeline:
    def __init__(self) -> None: 
        # variabile che farà riferimento al file csv 
        self.csv_path: str = "../dati/raw_data.csv"
        self.clean_csv_path = "../dati/clean_data.csv"
        self.output_plot = "../visual/scatter_plot.png"
    
    '''1) Lettura file csv'''
    def caricamento_dati(self) -> pd.DataFrame:
        # caricamento dati da un file .csv locale
        df = pd.read_csv(self.csv_path)
        # df.head()
        # df.tail()
        # df.describe()
        # df.dtypes()
        # df.info()
        return df
    
    '''4) Salvataggio dati'''
    def salvataggio_dati(self, df: pd.DataFrame) -> None:
        # Salvataggio dati su un file .csv locale 
        df.to_csv(self.clean_csv_path)

    '''3) Preprocessamento dati'''
    def preprocessamento_dati(self, df: pd.DataFrame) -> pd.DataFrame:
        # pulizia e preparazione dati

        # creo la nuova tabella se le due condizioni sono rispettati 
        df["is_healthy"] = (df["screen_time_hours"] < 4) & (df["sleep_hours"] >= 8)
        self.salvataggio_dati(df)
        return df
    
    '''5) Visualizzazione dati'''
    def visualizzazione_dati(self, df: pd.DataFrame) -> None:
        # visualizzazione dati
        plt.figure(figsize=(10,6))
        true_data: pd.DataFrame = df[df["is_healthy"] == True]
        false_data: pd.DataFrame = df[df["is_healthy"] == False]
        # chiama allo scatter 
        plt.scatter(true_data["screen_time_hours"], true_data["math_score"], color="green", label='True', alpha=0.7, s=100)
        plt.scatter(false_data["screen_time_hours"], false_data["math_score"], color="red", label='False', alpha=0.7, s=100)
        # alpha serve per gestire l'opacità del colore, s serve per gestire la domensione dei puntini
        plt.xlabel('Screen time hours')
        plt.ylabel('Math score')
        plt.title("Screen time hours vs Math score")
        plt.legend()
        plt.savefig(self.output_plot)
        plt.close()


        # plt.figure(figsize=(10,6))
        # # plt.xlabel('Screen time hours')
        # # plt.ylabel('Math score')
        # plt.title("Screen time hours vs Math score")
        # sns.scatterplot(data=df, x="screen_time_hours", y="math_score", hue="is_healthy")
        # # plt.legend()
        # plt.savefig(self.output_plot)
        # plt.close()


    '''2) Addestratori'''
    def esegui_pipeline(self)-> None:
        # caricamento
        raw_df = self.caricamento_dati()
        print("   -Letti dati da un file csv")
        # print(raw_df)
        # preprocessamento
        clean_df = self.preprocessamento_dati(raw_df)
        print("   -Pulizia dati completata e file pulito salvato")
        # print(clean_df.columns) 
        self.visualizzazione_dati(clean_df)
        print("   -Visualizzati e salvati risultati di analisi")

    
        

if __name__== "__main__":
    pipeline = DataPipeline()
    print("Pipeline avviata...")
    pipeline.esegui_pipeline()
    print("Pipeline completata con successo")
