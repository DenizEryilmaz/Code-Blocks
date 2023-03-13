class TreeNode:
    def __init__(self, data=None):
        # Bir düğüm oluşturur ve veri ve sol/sağ alt düğümlerini başlangıç değerlerine ayarlar
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        # BST oluşturur ve kök düğümünü başlangıç değerine ayarlar
        self.root = None

    def insert(self, data):
        # Veriyi BST'ye ekler
        new_node = TreeNode(data)
        if self.root is None:
            # BST boşsa, veriyi kök düğüm olarak ekler
            self.root = new_node
            return
        current = self.root
        # Verinin ekleneceği yeri bulur
        while True:
            if data < current.data:
                # Veri, mevcut düğümün verisinden küçükse, sol alt düğüme gider
                if current.left is None:
                    # Sol alt düğüm boşsa, veriyi sol alt düğüm olarak ekler
                    current.left = new_node
                    return
                current = current.left
            else:
                # Veri, mevcut düğümün verisinden büyükse veya eşitse, sağ alt düğüme gider
                if current.right is None:
                    # Sağ alt düğüm boşsa, veriyi sağ alt düğüm olarak ekler
                    current.right = new_node
                    return
                current = current.right

    def search(self, data):
        # Verinin BST'de olup olmadığını kontrol eder
        if self.root is None:
            # BST boşsa, veri yoktur
            return False
        current = self.root
        while current:
            # Verinin bulunup bulunmadığını araştırır
            if data == current.data:
                # Veri bulundu
                return True
            elif data < current.data:
                # Veri, mevcut düğümün verisinden küçükse, sol alt düğüme gider
                current = current.left
            else:
                # Veri, mevcut düğümün verisinden büyükse veya eşitse, sağ alt düğüme gider
                current = current.right
            # Veri bulunamadı
        return False

tree = BinarySearchTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)
print(tree.search(5)) # True
print(tree.search(6)) # True
print(tree.search(8)) # True
print(tree.search(1)) # False
