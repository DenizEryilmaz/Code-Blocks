# MSSQL veritabanı bağlantısını yapılandırın
db_server = 'server_name'
db_name = 'database_name'
db_user = 'user_name'
db_password = 'password'

# Sorgu için gereken veritabanı bağlantısını açın
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + db_server + ';DATABASE=' + db_name + ';UID=' + db_user + ';PWD=' + db_password)

# Girilen yaşı okuyun
age = int(input('Lütfen yaşınızı girin: '))

# Veritabanındaki "events" tablosundaki "min_age", "max_age" ve "activity" sütunlarındaki verileri çekin
cursor = conn.execute('SELECT min_age, max_age, activity FROM events')

# Kayıtları bir döngüde gezerek yaşın hangi aralıkta olduğunu bulun
for row in cursor:
    if row.min_age <= age <= row.max_age:
        # Yaşın aralıkta olduğu satırdaki etkinliği yazdırın
        print(row.activity)