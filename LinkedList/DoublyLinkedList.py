class Node:

    def __init__(self, data=None, next_node=None, previous_node=None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def get_previous(self):
        return self.previous_node

    def set_data(self, data):
        self.data = data

    def set_next(self, new_next_node):
        self.next_node = new_next_node

    def set_previous(self, new_previous_node):
        self.previous_node = new_previous_node


class DoublyLinkedList:

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
            self.head.set_previous(new_node)
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.count += 1

    def add_between(self, element, index):
        new_node = Node(element)
        p = self.head
        for i in range(index - 1):
            p = p.next_node
        q = p.next_node

        p.set_next(new_node)
        q.set_previous(new_node)

        new_node.set_next(q)
        new_node.set_previous(p)
        self.count += 1

    def add_last(self, element):
        new_node = Node(element)
        if self.tail:
            new_node.set_previous(self.tail)
            self.tail.set_next(new_node)
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node
        self.count += 1

    def remove_first(self):
        if self.count != 0:
            p = self.head.next_node
            self.head.set_next(None)
            self.head = p
            self.count -= 1
        else:
            raise ValueError('there is no value in list')

    def remove_between(self, index):
        if self.count != 0:
            p = self.head
            for i in range(index):
                p = p.next_node
            q = p.next_node
            r = p.previous_node

            p.set_next(None)
            p.set_previous(None)

            q.set_previous(r)
            r.set_next(q)
            self.count -= 1
        else:
            raise ValueError('there is no value in list')

    def remove_last(self):
        if self.count != 0:
            p = self.tail.previous_node
            p.set_next(None)
            self.tail.set_previous(None)
            self.tail = p
            self.count -= 1
        else:
            raise ValueError('there is no value in list')

    def printMyList(self):
        p = self.head
        for i in range(self.count):
            if p is not None:
                print(p.data, end=' ')
                p = p.next_node
        print()


DLL = DoublyLinkedList()
DLL.add_first(4)
DLL.add_first(3)
DLL.add_first(1)
DLL.add_between(2, 1)
DLL.printMyList()
# 1 2 3 4
DLL.remove_last()
DLL.remove_between(1)
DLL.remove_first()
DLL.printMyList()
# 3
