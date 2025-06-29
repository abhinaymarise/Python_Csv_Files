import pandas as pd

def read_csv_file():
    df=pd.read_csv(r"C:\Users\Abhinay\Documents\ETL\Pipelines\Question_7\order_data 1.csv")
    return df

df1=read_csv_file()
print(df1)