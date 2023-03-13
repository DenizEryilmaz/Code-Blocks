
import pymssql
# Sorgu için gereken veritabanı bağlantısını açın
conn =  pyodbc.connect(driver='{SQL Server}', server='(local)', database='reklamlar_db',
                       trusted_connection='yes')

# Girilen yaşı ve cinsiyeti okuyun
age = 5
gender = 1

# Veritabanındaki "events" tablosundaki "min_age", "max_age", "gender" ve "activity" sütunlarındaki verileri çekin
cursor = conn.execute('SELECT min_age, max_age, gender, reklam_görsel FROM reklamlar')

# Kayıtları bir döngüde gezerek yaşın hangi aralıkta olduğunu ve cinsiyetinin hangisi olduğunu bulun
for row in cursor:
    if row.min_age <= age <= row.max_age and (row.gender == gender or row.gender == '2'):
        # Yaşın aralıkta olduğu ve cinsiyetinin doğru olduğu satırdaki etkinliği yazdırın
        print(row.gender)