class set:

    # list is immutable type
    def __init__(self, list):
        self.new_list = []
        for i in range(len(list)):
            if list[i] not in self.new_list:
                self.new_list.append(list[i])
        print('[', end='')
        for j in range(len(self.new_list)):
            if j == len(self.new_list) - 1:
                print(self.new_list[j], end='')
            else:
                print(self.new_list[j], end=', ')
        print(']')


list1 = ['heelo', 'hi', 'nice', 'twp', 'hi', 'yes', 'heelo']
set(list1)



