# QUEUE ADT

class Node:
    def __init__(self, data):
        self.data, self.next = data, None

class Linked_list:
    def __init__(self):
        self.start = None

    def enqueu_linkedlist(self, ele):
        n = Node(ele)
        if self.start is None:
            self.start = n
        else:
            n.next = self.start
            self.start = n

    def dequeu_linkedlist(self):
        if self.start is None:
            print("list has no elements")
            return
        n = self.start
        if n.next is None:
            print("deleted ele", n.data)
            self.start = None
        else:
            while n.next.next:
                n = n.next
            print("deleted ele", n.next.data)
            n.next = None

    def display_list(self):
        if self.start is None:
            print("Empty Queue, Enter Value")
        else:
            t = self.start
            while t:
                print(t.data, end=" ")
                t = t.next
            print()

    def size(self):
        c, t = 0, self.start
        while t:
            c += 1
            t = t.next
        return c

if __name__ == '__main__':
    a = Linked_list()
    while True:
        print("\n1.Insert\t2.Delete\t3.Display\t4.Exit\t5.Size")
        ch = int(input("Enter your choice: "))
        if ch == 4:
            break
        elif ch == 1:
            ele = int(input("Enter your number: "))
            a.enqueu_linkedlist(ele)
            a.display_list()
        elif ch == 2:
            a.dequeu_linkedlist()
        elif ch == 3:
            a.display_list()
        elif ch == 5:
            print("Size of queue is =", a.size())
        else:
            print("INVALID OPTION")
