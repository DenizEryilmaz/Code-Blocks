class Queue:
    def __init__(self):
        # Kuyruk sınıfının ilk oluşturulmasında items listesi oluşturulur.
        # Bu liste, kuyrukta tutulacak verileri saklar.
        self.items = []

    def enqueue(self, item):
        # Bu method, kuyruğa yeni bir veri ekler.
        # Örneğin, enqueue(1) methodu çağırıldığında,
        # kuyruğa 1 değeri eklenir.
        self.items.append(item)

    def dequeue(self):
        # Bu method, kuyruktan ilk giren veriyi (FIFO prensibi) çıkarır
        # ve bu veriyi döndürür. Örneğin, kuyrukta 1, 2, 3 değerleri varsa
        # dequeue() methodu çağırıldığında 1 değeri çıkarılıp döndürülür.
        return self.items.pop(0)

    def peek(self):
        # Bu method, kuyruktaki ilk giren veriyi döndürür, ancak veriyi çıkarmaz.
        # Örneğin, kuyrukta 1, 2, 3 değerleri varsa peek() methodu çağırıldığında
        # 1 değeri döndürülür.
        return self.items[0]

    def is_empty(self):
        # Bu method, kuyruğun boş olup olmadığını kontrol eder.
        # Eğer kuyruk boşsa True, değilse False değerini döndürür.
        return not self.items

# Kuyruk sınıfından bir nesne oluşturulur.
queue = Queue()

# Kuyruğa veriler eklenir.
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)


print(queue.dequeue())
print(queue.peek())
print(queue.is_empty())
