class ArrayBasedStack:

    def __init__(self, size=5):
        self.stack = []
        self.size = size    # 입력한 size의 배열 생성
        self.count = 0      # 원소의 개수

    # top에 원소 쌓기 O(1)
    def push(self, element):
        if self.is_full():
            self.size *= 2
            self.stack.append(element)
        else:
            self.stack.append(element)
        self.count +=1

    # top에 있는 원소 제거 O(1)
    def pop(self):
        if self.is_empty():
            raise ValueError('value not in stack')
        else:
            del self.stack[-1]
            self.count -= 1

    # stack이 비어있는지 O(1)
    def is_empty(self):
        if self.stack:
            return False
        else:
            return True

    # stack이 꽉차있는지 O(1)
    def is_full(self):
        if self.count == self.size:
            return True
        else:
            return False

    # 원소의 개수 출력 O(1)
    def len(self):
        return self.count

    # top 원소가 무엇인지 O(1)
    def top(self):
        return self.stack[-1]

    # stack 출력
    def print_stack(self):
        if self.is_empty():
            raise ValueError('value not in stack')
        else:
            for i in range(self.count - 1, -1, -1):
                if i == self.count - 1:
                    print('│ %3d │ << top element' % self.stack[i])
                elif i == 0:
                    print('│ %3d │ << bottom element' % self.stack[i])
                else:
                    print('│ %3d │' % self.stack[i])
            print('└─────┘')


ABS = ArrayBasedStack()
ABS.push(12)
ABS.pop()
ABS.push(200)
ABS.push(100)
ABS.push(300)
ABS.print_stack()
ABS.pop()
ABS.pop()
ABS.pop()
print(ABS.is_full(), ABS.is_empty())

"""
│ 300 │ << top element
│ 100 │
│ 200 │ << bottom element
└─────┘
False True
"""


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