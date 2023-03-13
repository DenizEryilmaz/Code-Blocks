class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return not self.items

stack = Stack()
stack.push

"""
push: Stack'e yeni bir veri ekler.
pop: Stack'ten en son eklenen veriyi çıkarır ve döndürür.
peek: Stack'teki en son eklenen veriyi döndürür, ancak veriyi çıkarmaz.
isEmpty: Stack boş mu dolu mu olduğunu kontrol eder.
"""