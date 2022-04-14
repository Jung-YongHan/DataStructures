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


class LinkedListBasedStack:

    def __init__(self, head=None, tail=None):
        self.head = None
        self.tail = None
        self.stack = []
        self.count = 0

    def push(self, element):
        new_node = Node(element)
        if self.tail:
            p = self.tail
            p.set_next(new_node)
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise ValueError('value not in stack')
        else:
            p = self.head
            for i in range(self.count-1):
                p = p.next_node
            p.set_next(None)
            self.tail = p
        self.count -= 1

    def is_empty(self):
        if self.count != 0:
            return False
        else:
            return True

    def len(self):
        return self.count

    def print_stack(self):
        p = self.head
        if self.is_empty():
            raise ValueError('value not in stack')
        else:
            for i in range(self.count):
                print(p.element, end=' ')
                p = p.next_node
            print()


LLBS = LinkedListBasedStack()
LLBS.push(200)
LLBS.push(100)
LLBS.push(300)
LLBS.pop()
LLBS.pop()
LLBS.print_stack()