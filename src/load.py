from extract import df1
from util import mysql_get_engine

def load_data():
    engine=mysql_get_engine()
    try:
        data_frame=df1.to_sql("Orders",con=engine,if_exists='replace',index=False)
        print("Sent into MySql")
    except Exception as e:
        print("Work Hard,Come on you wil do it ")

if __name__=="__main__":
    load_data()