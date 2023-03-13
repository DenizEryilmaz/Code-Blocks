class HashTable:
    def __init__(self, size):
        # Özyinelemeli Harita sınıfının ilk oluşturulmasında size değişkeni
        # verilerek hash_table listesi oluşturulur. Bu liste, özyinelemeli
        # haritada saklanacak verilerin indekslerini tutar.
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        # Bu method, verilen anahtar değerine göre özyinelemeli haritada
        # hangi indekse yerleştirileceğini hesaplar. Örneğin, key değeri 10
        # ise hash_function(10) methodu çağırıldığında 0 değeri döndürülür.
        # Ancak key değeri 20 ise hash_function(20) methodu çağırıldığında
        # 0 değil, 10 değeri döndürülür. Bu sayede aynı anahtar değerleri
        # aynı indekse yerleştirilir.
        return key % self.size

    def insert(self, key, value):
        # Bu method, özyinelemeli haritaya yeni bir veri ekler.
        # Örneğin, insert(10, 'value1') methodu çağırıldığında,
        # 10 anahtar değerine ait 'value1' değeri özyinelemeli haritaya
        # eklenir.
        hash_key = self.hash_function(key)
        self.hash_table[hash_key].append((key, value))

    def search(self, key):
        # Bu method, özyinelemeli haritada verilen anahtar değere ait veriyi
        # arar ve bulursa bu veriyi, bulamazsa None değerini döndürür.
        # Örneğin, search(10) methodu çağırıldığında, 10 anahtar değerine
        # ait veri özyinelemeli haritada aranır ve eğer varsa bu veri,
        # yoksa None değeri döndürür
        hash_key = self.hash_function(key)
        for value in self.hash_table[hash_key]:
            if value[0] == key:
                return value[1]
        return None

hash_table = HashTable(10)
hash_table.insert(10, 'value1')
hash_table.insert(20, 'value2')
hash_table.insert(30, 'value3')
print(hash_table.search(10))
print(hash_table.search(20))
print(hash_table.search(30))
