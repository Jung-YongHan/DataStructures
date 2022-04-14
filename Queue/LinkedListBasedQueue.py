class Node(object):

    def __init__(self, element, next_node=None):
        self.element = element
        self.next_node = next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def get_next(self):
        return self.next_node

    def get_data(self):
        return self.element


class LinkedListBasedQueue:

    def __init__(self, head=None, tail=None):
        self.head = None
        self.tail = None
        self.queue = []
        self.count = 0

    def push(self, element):
        new_node = Node(element)
        if self.tail:
            self.tail.set_next(new_node)
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise ValueError('value not in queue')
        else:
            p = self.head
            for i in range(self.count-1):
                p = p.next_node
            p.set_next(None)
            self.tail = p
            self.count -= 1

    def pop_left(self):
        if self.is_empty():
            raise ValueError('value not in queue')
        else:
            p = self.head.next_node
            self.head.set_next(None)
            self.head = p
            self.count -= 1

    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False

    def first(self):
        return self.head.element

    def len(self):
        return self.count

    def print_queue(self):
        p = self.head
        for i in range(self.count):
            print(p.element, end=' ')
            p = p.next_node
        print()


LLBQ = LinkedListBasedQueue()
LLBQ.push(100)
LLBQ.push(200)
LLBQ.push(300)
LLBQ.push(400)
LLBQ.push(500)
LLBQ.pop()
LLBQ.pop_left()
print(LLBQ.first(), LLBQ.is_empty(), LLBQ.len())
LLBQ.print_queue()
