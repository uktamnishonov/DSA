class Stack:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return f"Stack: {self.items}"
    
    def __str__(self):
        return f"Stack: {self.items}"

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Cannot pop from an empty stack"
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"
    
    def size(self):
        return len(self.items)