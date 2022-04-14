class ArrayBasedList:

    def __init__(self, size):
        self.size = size
        self.List = size * [None]
        self.length = 0

    def len(self):
        return self.length

    # Indexing the element at j takes O(1) time
    def getItem(self, j):
        if self.length > j:
            return self.List[j]
        raise ValueError('value not in list')

    def setItem(self, val, j):
        if self.length > j:
            self.List[j] = val
            return
        raise ValueError('index is out of bound')

    """
    In the worst case (j = 0), this takes O(n) time
    When the array is full, instead of throwing an exception,
    we can replace the array with a larger one.
    """
    def insertItem(self, val , j=0):
        if self.size > j:
            self.length += 1

            if self.length > self.size:
                self.List += self.size * [None]
                self.size *= 2
            for i in range(self.size-1, j, -1):
                self.List[i] = self.List[i-1]
            self.List[j] = val
        else:
            while self.size <= j:
                self.List += self.size * [None]
                self.size *= 2
            self.length += 1
            for i in range(self.size-1, j, -1):
                self.List[i] = self.List[i-1]
            self.List[j] = val

    """
    In the worst case (j = 0), this takes O(n) time
    When the array is empty, throw an exception.
    """
    def removeItem(self, j=0):
        if self.length == 0:
            raise ValueError('the list is empty')
        else:
            if self.size <= j:
                raise ValueError('index is out of bound')
            else:
                for i in range(j+1, self.size):
                    if self.List[i] is None:
                        self.List[i-1] = self.List[i]
                        break
                    else:
                        self.List[i-1] = self.List[i]
                self.length -= 1

    def printMyList(self):
        for i in range(self.size):
            if self.List[i] is not None:
                print(self.List[i], end=' ')
        print()


ABL = ArrayBasedList(10)
ABL.insertItem(4)
ABL.insertItem(3)
ABL.insertItem(1)
ABL.insertItem(2, 1)
ABL.printMyList()
# 1 2 3 4
ABL.removeItem(3)
ABL.removeItem(1)
ABL.removeItem(0)
ABL.printMyList()
# 3
