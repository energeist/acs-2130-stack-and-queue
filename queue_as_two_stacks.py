from ll_stack import Stack

class QueueFromTwoStacks:
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
        
    def size(self):
        return (self.first_stack.size() + self.second_stack.size())
    
    def is_empty(self):
        return (self.first_stack.size() + self.second_stack.size()) == 0
        
    def front(self):
        if self.second_stack.is_empty():
            while not self.first_stack.is_empty():
                # print(self.first_stack.items.length())
                item = self.first_stack.pop().data
                # print(item)
                self.second_stack.push(item)
        return self.second_stack.peek()
    
    def enqueue(self, item):
        # This is O(1) worst case
        self.first_stack.push(item)
    
    def dequeue(self):
        # This becomes an O(n) operation instead of O(1) because we have to flip n items in the first stack
        if self.second_stack.is_empty():
            while not self.first_stack.is_empty():
                # print(self.first_stack.items.length())
                item = self.first_stack.pop().data
                # print(item)
                self.second_stack.push(item)
        return self.second_stack.pop().data

if __name__ == '__main__':        
    queue = QueueFromTwoStacks()
    print(f"Empty? {queue.is_empty()}")
    print("enqueue 3 elements")
    queue.enqueue(1) # Queue compostion: FRONT (1) BACK
    queue.enqueue(2) # Queue compostion: FRONT (1) -> (2) BACK
    queue.enqueue(3) # Queue compostion: FRONT (1) -> (2) -> (3) BACK
    print(f"Size: {queue.size()}")
    print(f"Empty? {queue.is_empty()}")
    print(f"Front: {queue.front()}")

    print("dequeue 2 elements")
    print(queue.dequeue()) # Stack should get flipped and should return 1
    print(queue.dequeue()) # Should return 2
    print(f"Size: {queue.size()}")
    print("enqueue 2 elements")
    queue.enqueue(4)
    queue.enqueue(5)
    print(f"Size: {queue.size()}")
    print("dequeue 1 element")
    print(queue.dequeue()) # Should return 3
    print(f"Size: {queue.size()}")