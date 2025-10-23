class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def inorder(root):
    if root:
        inorder(root.left); print(root.data, end=" "); inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=" "); preorder(root.left); preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left); postorder(root.right); print(root.data, end=" ")

if __name__ == "__main__":
    root = Node('A')
    root.left = Node('B'); root.right = Node('C')
    root.left.left = Node('D'); root.left.right = Node('E')
    root.right.right = Node('F')

    print("Inorder:"); inorder(root)
    print("\nPreorder:"); preorder(root)
    print("\nPostorder:"); postorder(root)
