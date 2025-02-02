class Pqueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return f"{self.queue}"
    
    def isEmpty(self):
        if len(self.queue) == 0:
            return f"True"
        else:
            return f"False"
    
    def insert(self,val):
        self.queue.append(val)
        self.queue.sort()

    def delete(self):
        self.queue.sort()
        self.queue.pop()

    