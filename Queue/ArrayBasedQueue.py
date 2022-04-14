class ArrayBasedQueue:

    def __init__(self, size=5):
        self.queue = []
        self.size = size
        self.count = 0

    def push(self, element):
        if self.is_full():
            self.size *= 2
            self.queue.append(element)
        else:
            self.queue.append(element)
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise ValueError('value not in queue')
        else:
            del self.queue[-1]
            self.count -= 1

    def pop_left(self):
        if self.is_empty():
            raise ValueError('value not in queue')
        else:
            del self.queue[0]
            self.count -= 1

    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.count == self.size:
            return True
        else:
            return False

    def first(self):
        return self.queue[0]

    def last(self):
        return self.queue[-1]

    def len(self):
        return self.count

    def print_queue(self):
        for i in range(self.count):
            print(self.queue[i], end=' ')


ABQ = ArrayBasedQueue()
ABQ.push(100)
ABQ.push(200)
ABQ.push(300)
ABQ.push(400)
ABQ.push(500)
ABQ.pop()
ABQ.pop_left()
print(ABQ.is_full(), ABQ.is_empty(), ABQ.len())
ABQ.print_queue()