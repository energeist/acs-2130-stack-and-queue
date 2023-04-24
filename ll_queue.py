from linkedlist import LinkedList

class Queue(object):
    def __init__(self):
        self.items = LinkedList()

    def size(self):
        # O(n) worst case
        return self.items.length()

    def is_empty(self):
        # O(n) worst case
        return self.items.length() == 0
    
    def front(self):
        # O(1) worst case time complexity
        if self.items.head:
            return self.items.head

    def enqueue(self, item):
        # O(1) worst case time complexity
        self.items.append(item)

    def dequeue(self):
        # O(1) worst case time complexity
        item = self.items.head
        self.items.head = item.next
        item.next = None
        return item

my_queue = Queue()

if __name__ == '__main__':
    print(f"Size: {my_queue.size()}") # 0
    print(f"Empty?: {my_queue.is_empty()}") # True
    print("Enqueueing")
    my_queue.enqueue(100)
    my_queue.enqueue(5)
    my_queue.enqueue(20)
    print(f"Size: {my_queue.size()}") # Should return 3
    print(f"Front: {my_queue.front().data}")
    print(f"items: FRONT || {my_queue.items}|| BACK") # FRONT || (100) -> (5) -> (20) -> || BACK
    print("dequeueing")
    item = my_queue.dequeue().data
    print(f"dequeued item: {item}") # should return 100
    item = my_queue.dequeue().data
    print(f"dequeued item: {item}") # should return 5
    print(f"Size: {my_queue.size()}") # Should return 1
    print(f"items: FRONT || {my_queue.items}|| BACK") # FRONT || (20) -> || BACK
    my_queue.enqueue(99)
    my_queue.enqueue(1234)
    print(f"Size: {my_queue.size()}") # Should return 3
    print(f"items: FRONT || {my_queue.items}|| BACK") # FRONT || (20) -> (99) -> (1234) || BACK