class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_data(self, data):
        self.data = data

    def set_next(self, new_next_node):
        self.next_node = new_next_node


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def len(self):
        return self.count

    def getItem(self, index):
        if self.count > index:
            p = self.head
            for i in range(index):
                p = p.next_node
            return p.data
        raise ValueError('value not in list')

    def add_first(self, element):
        new_node = Node(element)
        if self.head:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.count += 1

    def add_last(self, element):
        new_node = Node(element)
        if self.tail:
            self.tail.set_next(new_node)
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node
        self.count += 1

    def remove_first(self):
        p = self.head
        self.head = p.next_node
        p.set_next(None)
        self.count -= 1

    def remove_last(self):
        p = self.head
        for i in range(self.count-1):
            p = p.next_node
        self.tail = p
        p.set_next(None)
        self.count -= 1

    def print_Linked_List(self):
        p = self.head
        for i in range(self.count):
            print(p.data, end=' ')
            p = p.next_node
        print()


SLL = SinglyLinkedList()
SLL.add_first(3)
SLL.add_last(1)
SLL.add_last(0)
SLL.remove_first()
SLL.print_Linked_List()
print(SLL.len())
print(SLL.getItem(0))
