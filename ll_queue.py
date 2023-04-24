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
    print("Size:")
    print(my_queue.size())
    print("Empty?")
    print(my_queue.is_empty())
    print("Enqueueing")
    my_queue.enqueue(100)
    my_queue.enqueue(5)
    my_queue.enqueue(20)

    print("Size:")
    print(my_queue.size())

    print("items:")
    print(my_queue.items)

    print("dequeueing")
    my_queue.dequeue()
    print(my_queue.items.head)
    my_queue.dequeue()

    print(my_queue.items)