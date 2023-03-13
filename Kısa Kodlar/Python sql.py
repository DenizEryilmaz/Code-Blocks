
import pyodbc
# MSSQL veritabanı bağlantısını yapılandırın
db_server = 'server_name'
db_name = 'database_name'
db_user = 'user_name'
db_password = 'password'

# Sorgu için gereken veritabanı bağlantısını açın
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + db_server + ';DATABASE=' + db_name + ';UID=' + db_user + ';PWD=' + db_password)
cursor = conn.execute('SELECT * FROM events')
