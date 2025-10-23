class Stack:
    def __init__(self): self.items = []
    def push(self, x): self.items.append(x)
    def pop(self): return self.items.pop() if self.items else None
    def peek(self): return self.items[-1] if self.items else None
    def empty(self): return len(self.items) == 0

def prec(op): return {'+':1,'-':1,'*':2,'/':2,'^':3}.get(op,0)
def isopnd(ch): return ch.isalnum()

def infix_to_postfix(expr):
    s, out = Stack(), ""
    for ch in expr:
        if isopnd(ch): out += ch
        elif ch == '(': s.push(ch)
        elif ch == ')':
            while not s.empty() and s.peek()!='(': out += s.pop()
            s.pop()
        else:
            while not s.empty() and prec(ch) <= prec(s.peek()): out += s.pop()
            s.push(ch)
    while not s.empty(): out += s.pop()
    return out

if __name__ == "__main__":
    e = input("Enter infix: ")
    print("Postfix:", infix_to_postfix(e))
