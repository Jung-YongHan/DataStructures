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

