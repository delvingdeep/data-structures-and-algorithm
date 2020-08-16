class Stack:
    def __init__(self):
        self.arr = [None]
        self.next_item = 0
        self.num_elements = 0


    def push(self, data):

        # if stack is empty
        if self.num_elements == 0:
            self.arr = [data]
            self.next_item = 1
            self.num_elements = 1
            return

        # else push old elements in stack and add one
        new_arr = [None] * (self.num_elements+1)

        for i in range(self.num_elements):
            new_arr[i] = self.arr[i]
        new_arr[self.next_item] = data

        self.arr = new_arr
        self.next_item += 1
        self.num_elements += 1
        return

    def size(self):
        return self.num_elements

    def is_empty(self):
        if self.num_elements == 0:
            return True
        return False


if __name__ == '__main__':
    foo = Stack()

    # test is_empty method
    print('Is foo empty: ', foo.is_empty())

    # test push method
    foo.push('Hello')
    foo.push('World')
    foo.push(3)

    print('foo array: ', foo.arr)
    print('Is foo empty: ', foo.is_empty())

    # test size method
    print('Size of foo stack: ', foo.size())

