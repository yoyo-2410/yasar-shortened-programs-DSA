# Binary Search Tree

class Node:
    def __init__(self, d):
        self.d, self.l, self.r = d, None, None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, d, node=None):
        if not self.root:
            self.root = Node(d); return
        node = node or self.root
        if d < node.d:
            if node.l: self.insert(d, node.l)
            else: node.l = Node(d)
        elif d > node.d:
            if node.r: self.insert(d, node.r)
            else: node.r = Node(d)
        else:
            print("Duplicate value!")

    def search(self, d, node=None):
        node = node or self.root
        if not node: return False
        if node.d == d: return True
        return self.search(d, node.l) if d < node.d else self.search(d, node.r)

    def display(self, n, lvl=0, pre="Root: "):
        if n:
            print(" " * (lvl*4) + pre + str(n.d))
            self.display(n.l, lvl+1, "L--- ")
            self.display(n.r, lvl+1, "R--- ")

bst = BST()
while True:
    print("\n1.Insert  2.Search  3.Display  4.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        bst.insert(int(input("Enter value: ")))
    elif ch == 2:
        v = int(input("Enter value to search: "))
        print("Found" if bst.search(v) else "Not Found")
    elif ch == 3:
        bst.display(bst.root)
    else:
        break
