import time

minutes = 0

while True:
    print("Dakika sayısı:", minutes)
    minutes += 1
    time.sleep(60)  # 60 saniye bekleyin ve tekrar başlayın

#Bu kod google colab üzerinden indirme yaparken aktif olunmadığında
#zaman aşımından dolayı oturumun kapanmaması içinoturumu meşgul
#etmek için kullanılmaktadır