import os
import sys
#from src.exception import CustomException
#from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    cwdir=os.getcwd()
    print(cwdir)
    train_data_path: str=os.path.join(cwdir,'artifacts',"train.csv")
    test_data_path: str=os.path.join(cwdir,'artifacts',"test.csv")
    raw_data_path: str=os.path.join(cwdir,'artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        #logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv(r'C:\Data_Science_by_krish\udemy_practice_notes\mlproject\notebook\data\stud.csv')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            print(e)
        
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()


