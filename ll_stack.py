from linkedlist import LinkedList

class Stack(object):
    def __init__(self):
        self.items = LinkedList()
        
    def size(self):
        return self.items.length()
    
    def is_empty(self):
        return self.items.length() == 0
        
    def push(self, new_data):
        # O(1) worst case time complexity
        self.items.prepend(new_data)

    def pop(self):
        # O(1) worst case time complexity
        item = self.items.head
        self.items.head = item.next
        item.next = None
        return item

    def peek(self):
        # O(1) worst case time complexity
        if self.items.head:
            return self.items.head.data

if __name__ == '__main__':
    print("stack tests")
    stack = Stack()
    print(stack.is_empty())
    stack.push("A")
    stack.push("C")
    stack.push("B")
    print("peek: ")  # should be B
    print(stack.peek())
    stack.pop()
    stack.pop()
    stack.pop()
    print("peek: ")  # should be C
    print(stack.peek())
    stack.push("X")
    stack.push("Z")
    print("peek: ")  # should be Z
    print(stack.peek())