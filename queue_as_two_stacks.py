from ll_stack import Stack

class QueueFromTwoStacks():
    # We will use two stacks, one to push to and one to pop from.
    # We will continuously push to one stack until we want to pop. 
    # If the second stack is empty then the first stack is reversed onto a second stack
    # by popping each element from the first stack and pushing
    # to the second stack, which will leave the top element of the second stack as the 
    # first element that was pushed to the first stack.  If the second stack is already 
    # populated then we can just pop from it until is_empty is true, then we have to flip the
    # first stack again.  Popping this top element from the second stack emulates the FIFO 
    # behaviour of a queue.
    
    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()
    
    def enqueue(self, item):
        # This is O(1) worst case
        self.first_stack.push(item)
    
    def dequeue(self):
        # This becomes an O(n) operation instead of O(1) because we have to flip n items in the first stack
        if self.second_stack.is_empty():
            while self.first_stack.items.length() > 0:
                # print(self.first_stack.items.length())
                item = self.first_stack.pop().data
                # print(item)
                self.second_stack.push(item)
        return self.second_stack.pop().data
        
queue = QueueFromTwoStacks()
print("enqueue 3 elements")
queue.enqueue(1) # Stack compostion: TOP (1) BOTTOM
queue.enqueue(2) # Stack compostion: TOP (1) -> (2) BOTTOM
queue.enqueue(3) # Stack compostion: TOP (1) -> (2) -> (3) BOTTOM
print("peek at top element")
print(queue.first_stack.peek()) # Should return 3

print("dequeue 2 elements")
print(queue.dequeue()) # Stack should get flipped and should return (1)
print(queue.dequeue()) # Should return (2)

queue.enqueue(4)
queue.enqueue(5)
print("peek at top element") # Should return 5
print("dequeue 1 element")
print(queue.dequeue()) # Should return 3
