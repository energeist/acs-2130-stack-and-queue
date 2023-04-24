from ll_queue import Queue

class StackFromTwoQueues:
    def __init__(self):
        self.first_queue = Queue()
        self.second_queue = Queue()
        
    def size(self):
        pass
    
    def is_empty(self):
        pass
        
    def push(self, new_data):
        while not self.first_queue.is_empty():
            self.second_queue.enqueue(self.first_queue.dequeue().data)
        self.first_queue.enqueue(new_data)
        while not self.second_queue.is_empty():
            self.first_queue.enqueue(self.second_queue.dequeue().data)

    def pop(self):
        size = self.first_queue.size()
        i = 0
        while i < size - 1:
            item = self.first_queue.dequeue().data
            self.second_queue.enqueue(item)
            i += 1
        item = self.first_queue.dequeue().data
        while not self.second_queue.is_empty():
            self.first_queue.enqueue(self.second_queue.dequeue().data)
        return item
    
    def peek(self):
        pass


class StackFromOneQueue:
    def __init__(self):
        self.stack = Queue()
        
if __name__ == '__main__': 
    stack = StackFromTwoQueues()
    stack.push(1) # Stack structure: TOP (1) BOTTOM
    stack.push(2) # Stack structure: TOP (2) -> (1) BOTTOM
    stack.push(3) # Stack structure: TOP (3) -> (2) -> (1) BOTTOM
    print(stack.pop()) # should return 3
    print(stack.pop()) # should return 2
        

