class Node:
    def __init__(self, data=None):
        # Node sınıfının ilk oluşturulmasında data değişkeni verilerek
        # data ve next değişkenleri oluşturulur. Bu değişkenler, bağlı
        # listede tutulacak verileri ve bir sonraki verinin adresini
        # saklar.
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Bağlı Liste sınıfının ilk oluşturulmasında head değişkeni
        # oluşturulur. Bu değişken, bağlı liste içindeki ilk verinin
        # adresini saklar.
        self.head = None

    def append(self, data):
        # Bu method, bağlı listeye yeni bir veri ekler.
        # Örneğin, append(1) methodu çağırıldığında, bağlı listeye 1
        # değeri eklenir.
        new_node = Node(data)

        # Eğer bağlı liste boşsa, head değişkenine yeni verinin adresi
        # atanır.
        if self.head is None:
            self.head = new_node
            return

        # Bağlı liste boş değilse, head değişkeninin next değişkenine
        # gidilerek en son veri bulunur.
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def prepend(self, data):
        """Bu kod, bağlı listeye en başa yeni bir veri eklemek için kullanılır.
         Örneğin, prepend(1) methodu çağırıldığında, bağlı listeye 1 değeri en başa eklenir.

        Bu method içinde öncelikle new_node adında yeni bir Node nesnesi oluşturulur
        ve data değişkeni verilerek bu nesnenin data değişkenine atanır. Daha sonra,
        new_node nesnesinin next değişkenine mevcut self.head değişkeninin adresi atanır.
        Bu sayede, bağlı listede mevcut olan ilk veri ile yeni veri arasında bağ oluşturulur.
        Son olarak, self.head değişkenine yeni verinin adresi atanır ve bu sayede
        yeni veri bağlı listede en başa eklenmiş olur."""

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, data):
        """Bu kod, bağlı liste içinde verilen data değerine sahip olan veriyi silmek için kullanılır.
         Örneğin, delete_node(1) methodu çağırıldığında, bağlı liste içinde 1 değerine sahip olan veri silinir.

        Bu method içinde öncelikle, bağlı liste boşsa hiçbir işlem yapılmaz ve methoddan çıkılır.
        Eğer bağlı liste boş değilse, self.head değişkeninin data değişkenine bakılır ve eğer bu değişken
        verilen data değerine eşitse, self.head değişkenine bir sonraki verinin adresi atanır ve methoddan çıkılır.
        Bu sayede, bağlı listede ilk veri silinmiş olur.

        Eğer self.head değişkeninin data değişkeni verilen data değerine eşit değilse, current değişkenine
        self.head değişkeninin adresi atanır ve current değişkeni ile current.next arasındaki veriler gezilerek aranır.
        Eğer current.next.data değişkeni verilen data değerine eşitse, current.next değişkenine
        bir sonraki verinin adresi atanır ve methoddan çıkılır. Bu sayede, aranan veri silinmiş olur.
        Eğer aranan veri bulunamazsa, current değişkenine bir sonraki verinin adresi atanır.
        Eğer döngü tamamlanır ve eşleşme bulunmazsa, yöntem değişiklik yapmadan döner."""
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def print_list(self):
        """Bu yöntem, bir bağlı liste içindeki tüm düğümlerin verilerini yazdırır.
        Yöntem, bağlı listenin baş düğümünü mevcut düğüm olarak ayarlar ve daha sonra
        mevcut düğümün None olup olmadığına bakarak bir döngüye girer.
        Eğer mevcut düğüm None değilse, mevcut düğümün verisini yazdırır
        ve mevcut düğümü "next" referansı olarak günceller.
        Bu işlemler, mevcut düğüm None olana kadar devam eder.
        Bu sayede, bağlı listenin tüm düğümleri yazdırılır."""
        current = self.head
        while current:
            print(current.data)
            current = current.next

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.prepend(0)
linked_list.delete_node(2)
linked_list.print_list()
