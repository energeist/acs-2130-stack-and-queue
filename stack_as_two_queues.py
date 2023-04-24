from ll_queue import Queue

class StackFromTwoQueues:
    def __init__(self):
        self.first_queue = Queue()
        self.second_queue = Queue()
        
    def size(self):
        return (self.first_queue.size() + self.second_queue.size())
    
    def is_empty(self):
        return (self.first_queue.size() + self.second_queue.size()) == 0
        
    def push(self, new_data):
        while not self.first_queue.is_empty():
            self.second_queue.enqueue(self.first_queue.dequeue().data)
        self.first_queue.enqueue(new_data)
        while not self.second_queue.is_empty():
            self.first_queue.enqueue(self.second_queue.dequeue().data)

    def pop(self):
        return self.first_queue.dequeue().data
    
    def peek(self):
        return self.first_queue.front().data

class StackFromOneQueue:
    def __init__(self):
        self.stack = Queue()
        
    def size(self):
        return (self.stack.size())
    
    def is_empty(self):
        return (self.stack.size()) == 0
        
    def push(self, new_data):
        self.stack.enqueue(new_data)
        size = self.stack.size()
        i = 0
        while i < size - 1:
            self.stack.enqueue(self.stack.dequeue().data)
            i += 1
            
    def pop(self):
        return self.stack.dequeue().data
    
    def peek(self):
        return self.stack.front().data
        
if __name__ == '__main__':
    print("Stack from two queues:") 
    stack = StackFromTwoQueues()
    print(f"Size: {stack.size()}")
    print(f"Empty? {stack.is_empty()}")
    print("Push 3 items")
    stack.push(1) # Stack structure: TOP (1) BOTTOM
    stack.push(2) # Stack structure: TOP (2) -> (1) BOTTOM
    stack.push(3) # Stack structure: TOP (3) -> (2) -> (1) BOTTOM
    print(f"Size: {stack.size()}")
    print(f"Empty? {stack.is_empty()}")
    print(f"Peek: {stack.peek()}") # Should return 3
    print("Pop 2 elements")
    print(stack.pop()) # should return 3
    print(stack.pop()) # should return 2
    print(f"Size: {stack.size()}")
    print("Push one element")
    stack.push(4) # Stack structure: TOP (4) -> (1) BOTTOM
    print(f"Size: {stack.size()}")
    print(f"Peek: {stack.peek()}") # Should return 4
    print("Pop 2 elements")
    print(stack.pop()) # should return 4
    print(stack.pop()) # should return 1
    print(f"Size: {stack.size()}")
    print(f"Empty? {stack.is_empty()}")
    
    print("\nStack from one queue:") 
    stack = StackFromOneQueue()
    print(f"Size: {stack.size()}")
    print(f"Empty? {stack.is_empty()}")
    print("Push 3 items")
    stack.push(1) # Stack structure: TOP (1) BOTTOM
    stack.push(2) # Stack structure: TOP (2) -> (1) BOTTOM
    stack.push(3) # Stack structure: TOP (3) -> (2) -> (1) BOTTOM
    print(f"Size: {stack.size()}")
    print(f"Empty? {stack.is_empty()}")
    print(f"Peek: {stack.peek()}") # Should return 3
    print("Pop 2 elements")
    print(stack.pop()) # should return 3
    print(stack.pop()) # should return 2
    print(f"Size: {stack.size()}")
    print("Push one element")
    stack.push(4) # Stack structure: TOP (4) -> (1) BOTTOM
    print(f"Size: {stack.size()}")
    print(f"Peek: {stack.peek()}") # Should return 4
    print("Pop 2 elements")
    print(stack.pop()) # should return 4
    print(stack.pop()) # should return 1
    print(f"Size: {stack.size()}")
    print(f"Empty? {stack.is_empty()}")
    
    
        

