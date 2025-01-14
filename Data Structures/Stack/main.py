from stack import *

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Stack size:", stack.size())
print("Top element:", stack.peek())
print("Popped item:", stack.pop())
print("Stack size:", stack.size())
print("Is stack empty? ", stack.is_empty())
