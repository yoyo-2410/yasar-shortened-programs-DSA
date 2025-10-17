# Doubly Linked List ADT

class Node:
    def __init__(self, data):
        self.data, self.next, self.prev = data, None, None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        n = Node(data)
        if self.head:
            n.next, self.head.prev = self.head, n
        self.head = n
        print(f"Inserted {data} at the start.")

    def insert_at_end(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
        else:
            t = self.head
            while t.next:
                t = t.next
            t.next, n.prev = n, t
        print(f"Inserted {data} at the end.")

    def delete_from_start(self):
        if not self.head:
            print("List is empty, nothing to delete.")
        else:
            print(f"Deleted {self.head.data} from the start.")
            self.head = self.head.next
            if self.head: self.head.prev = None

    def delete_from_end(self):
        if not self.head:
            print("List is empty, nothing to delete.")
        else:
            t = self.head
            if not t.next:
                print(f"Deleted {t.data} from the end.")
                self.head = None
            else:
                while t.next: t = t.next
                print(f"Deleted {t.data} from the end.")
                t.prev.next = None

    def display(self):
        if not self.head:
            print("List is empty.")
        else:
            t = self.head
            while t:
                print(t.data, end=" ")
                t = t.next
            print()

if __name__ == "__main__":
    dll = DoublyLinkedList()
    while True:
        print("\nDoubly Linked List Operation:\n-----------------------------")
        print("1. Insert at start\n2. Insert at end\n3. Delete from start\n4. Delete from end\n5. Display list\n6. Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1: dll.insert_at_start(int(input("Enter data: ")))
        elif ch == 2: dll.insert_at_end(int(input("Enter data: ")))
        elif ch == 3: dll.delete_from_start()
        elif ch == 4: dll.delete_from_end()
        elif ch == 5: dll.display()
        elif ch == 6: print("Exiting..."); break
        else: print("Invalid choice! Please try again.")
