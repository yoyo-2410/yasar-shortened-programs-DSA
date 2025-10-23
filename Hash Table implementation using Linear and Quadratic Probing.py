class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None]*size

    def hash_func(self, key):
        return key % self.size

    def insert_linear(self, key):
        for i in range(self.size):
            idx = (self.hash_func(key)+i) % self.size
            if self.table[idx] is None:
                self.table[idx] = key; return
        print("Table Full (Linear)")

    def insert_quadratic(self, key):
        for i in range(self.size):
            idx = (self.hash_func(key)+i*i) % self.size
            if self.table[idx] is None:
                self.table[idx] = key; return
        print("Table Full (Quadratic)")

    def display(self):
        for i,v in enumerate(self.table):
            print(i, ":", v)

print("=== Linear Probing ===")
h1 = HashTable(10)
for k in [23,43,13,27,33]: h1.insert_linear(k)
h1.display()

print("\n=== Quadratic Probing ===")
h2 = HashTable(10)
for k in [23,43,13,27,33]: h2.insert_quadratic(k)
h2.display()
