class Queue:
    def __init__(self):
        self.items = []

    def enque(self,item):
        self.items.append(item)

    def deque(self):
        del self.items[0]

    def size(self):
        return len(self.items)
    
    def peek(self):
        if not self.items:
            return f"Queue is empty" 
        else:
            return self.items[0]
    
    def __str__(self):
        return f"{self.items}"