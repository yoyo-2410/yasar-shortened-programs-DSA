# STACK ADT

class Node:
    def __init__(self, data):
        self.data, self.next = data, None

class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, data):
        n = Node(data)
        n.next, self.top = self.top, n

    def pop(self):
        if self.isempty():
            print("Stack empty")
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        return None if self.isempty() else self.top.data

    def display(self):
        iternode = self.top
        if self.isempty():
            print("Stack Underflow")
        else:
            while iternode is not None:
                print(iternode.data, end="")
                iternode = iternode.next
                if iternode is not None:
                    print("-> ", end="")
            print()

# Driver (keeps original prompts & outputs)
if __name__ == "__main__":
    Mystack = Stack()
    while True:
        print("\n")
        print(" STACK OPERATION")
        print("------------------------------\n")
        print("\nSELECT APPROPRIATE CHOICE")
        print("1. PUSH Element into Stack")
        print("2. POP Element from stack ")
        print("3. Display Elements in the stack")
        print("4. Exit")

        choice = int(input("Enter the Choice: "))

        if choice == 1:
            n = int(input("Enter number of elements to push into stack: \n"))
            for i in range(n):
                element = int(input(f"Enter element {i + 1} to add to the stack: "))
                Mystack.push(element)

        elif choice == 2:
            popped = Mystack.pop()
            if popped is not None:
                print(f"The topmost node ({popped}) deleted")

        elif choice == 3:
            Mystack.display()

        elif choice == 4:
            break
