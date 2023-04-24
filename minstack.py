from linkedlist import LinkedList

class MinStack:
    def __init__(self):
        self.items = LinkedList()
        self.min = None
            
    def get_min(self):
        if self.items.head:
            return self.min
        else:
            return "The stack is empty!" 
        
    def size(self):
        return self.items.length()
    
    def is_empty(self):
        return self.items.length() == 0
        
    def push(self, new_data):
        # O(1) worst case time complexity
        # if there is no minimum value, the stack is empty and the first value pushed is the new minimum
        if not self.min:
            self.min = new_data
            self.items.prepend(new_data)
        # if new data is less than the minimum value, hold the previous minimum in a temp variable
        # and transform it in a way that it can be tracked recursively, so that we can support
        # many operations that would change self.min
        elif (new_data < self.min):
            hold = (2 * new_data) - self.min
            self.items.prepend(hold)
            self.min = new_data
        # else, value of new data is greater than minimum value and does not need to be tracked
        else:
            self.items.prepend(new_data)

    def pop(self):
        # O(1) worst case time complexity
        if not self.items.head:
            return "The stack is empty!"
        else:
            item = self.items.head
            self.items.head = item.next
            item.next = None
            if item.data < self.min:
                self.min = ((2 * self.min) - item.data)
            return item

    def peek(self):
        # O(1) worst case time complexity
        if self.items.head:
            return self.items.head.data
        
if __name__ == '__main__':
   
  stack = MinStack()
   
  # Function calls
  stack.push(3)
  stack.push(5)
  print(stack.get_min()) # Should return 3
  stack.push(2)
  stack.push(1)
  print(stack.get_min()) # Should return 1
  stack.pop()
  print(stack.get_min()) # Should return 2
  stack.pop()
  print(stack.get_min()) # Should return 3
  print(stack.peek()) # Should return 5
  stack.pop()
  stack.pop()
  print(stack.pop()) # Should return "The stack is empty!"
  print(stack.get_min()) # Should return "The stack is empty!"
  