class Node:

    def __init__(self, k, v):
        self.key = k
        self.value = v


class Heap:

    def __init__(self):
        self.data = []
        self.root = None
        self.last_node = None
        self.count = 0

    def add(self, k, v):
        new_node = Node(k, v)
        if self.root:
            self.data.append(new_node)
        else:
            self.root = new_node
            self.data.append(new_node)
        self.last_node = new_node
        self.count += 1
        cur_index = self.count - 1
        while True:  # up_heap
            if cur_index >= 2:
                parent_index = (cur_index - 1) // 2
                if self.data[cur_index].key < self.data[parent_index].key:
                    self.data[parent_index], self.data[cur_index] = self.data[cur_index], self.data[parent_index]
                cur_index = parent_index
            else:
                if self.data[cur_index].key < self.data[0].key:
                    self.data[cur_index], self.data[0] = self.data[0], self.data[cur_index]
                break
        self.root = self.data[0]

    def remove_min(self):
        self.data[0] = self.data[-1]
        del self.data[-1]
        self.count -= 1
        current = 0
        while True:  # down_heap
            left = current * 2 + 1
            right = current * 2 + 2
            if self.count > right:
                if self.data[left].key < self.data[right].key:
                    min_node_index = left
                else:
                    min_node_index = right

                if self.data[current].key > self.data[min_node_index].key:
                    self.data[current], self.data[min_node_index] = self.data[min_node_index], self.data[current]
                    current = min_node_index
                else:
                    break
            else:
                break

    def printHeap(self):
        for i in range(self.count):
            print('({},{}) <-- \'{}\'node'.format(self.data[i].key, self.data[i].value, i))


s = Heap()
s.add(3, 4)
s.add(10, 2)
s.add(4, 7)
s.add(8, 1)
s.add(1, 6)
s.add(5, 7)
"""
(1,6) <-- '0'node
(3,4) <-- '1'node
(4,7) <-- '2'node
(10,2) <-- '3'node
(8,1) <-- '4'node
(5,7) <-- '5'node
"""
s.remove_min()
s.remove_min()
s.remove_min()
"""
(5,7) <-- '0'node
(10,2) <-- '1'node
(8,1) <-- '2'node
"""
s.printHeap()