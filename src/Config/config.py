#By using Sql Server Credentials
ms_db_config={   
    'dialect':'mssql+pyodbc',
    'server':'DESKTOP-4IVU8N4\MSSQLSERVER1',
    'username':'sa',     
    'password':'abcd',     
    'Driver':'ODBC Driver 17 for SQL server',     
    'Database':'Pipelines',
    'Driver':'ODBC+Driver+17+for+SQL+Server' 
    }

#Direct_connection_Url
ms_connection_url="mssql+pyodbc://sa:abcd@DESKTOP-4IVU8N4\MSSQLSERVER1/Pipelines?Driver=Odbc+Driver+17+for+SQL+Server"

#By using MySql Credentials

mysql_db_config={
    'host':'localhost',
    'port': 3306,
    'username':'root',
    'password':'admin123',
    'database':'python_etl'
}

#Direct_Connection_Url
mysql_connecton_url='mysql+mysqlconnector://root:admin123@localhost:3306/python_etl'

