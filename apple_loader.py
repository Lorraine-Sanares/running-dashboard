import pandas as pd

class DataSchema:
    VO2_MAX = 'value'
    DATE = 'start_date'

def load_apple_data(path: str) -> pd.DataFrame:
    
    
    def clean_vo2max(path: str) -> pd.DataFrame:
        df = pd.read_csv(path) # accesing V02 max csv, 2nd in the list
        df['startDate'] = pd.to_datetime(df['startDate'], format='mixed')
        df['start_date'] = df['startDate'].dt.date
        cols = ['start_date', 'value'] # selecting relevant cols
        df = df[cols]
        return df
    data = clean_vo2max(path)
    
    return data