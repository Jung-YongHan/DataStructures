class Item:

    def __init__(self, k, v):
        self.key = k
        self.value = v


class PriorityQueue:

    def __init__(self):
        self.data = []
        self.count = 0

    def add(self, k, v):
        new_item = Item(k,v)
        self.data.append(new_item)
        self.count += 1

    def remove_min(self):
        if self.is_empty():
            raise ValueError('value not in PQ')
        else:
            min_key = self.data[0].key
            min_key_index = 0
        for i in range(1, self.count):
            if min_key > self.data[i].key:
                min_key_index = i
        del self.data[min_key_index]
        self.count -= 1

    def min(self):
        if self.is_empty():
            raise ValueError('value not in PQ')
        else:
            min_key = self.data[0].key
            min_key_index = 0
        for i in range(1, self.count):
            if min_key > self.data[i].key:
                min_key_index = i
        return self.data[min_key_index].key, self.data[min_key_index].value

    def len(self):
        print(self.count)

    def is_empty(self):
        return self.count == 0

    def printPQ(self):
        print('{',end='')
        for i in range(self.count):
            if i == self.count-1:
                print('({},{})'.format(self.data[i].key, self.data[i].value), end='')
            else:
                print('({},{})'.format(self.data[i].key, self.data[i].value), end=',')
        print('}')


PQ = PriorityQueue()
PQ.add(5, 'A')
PQ.add(9, 'C')
PQ.add(3, 'B')
PQ.add(7, 'D')
PQ.printPQ()
PQ.min()
PQ.remove_min()
PQ.remove_min()
PQ.printPQ()
PQ.len()
print(PQ.is_empty())
"""
{(5,A),(9,C),(3,B),(7,D)}
(3,B)
{(9,C),(7,D)}
2
False
"""

