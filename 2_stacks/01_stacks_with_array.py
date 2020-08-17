class Stack:
    def __init__(self):
        self.arr = [None]
        self.next_index = 0
        self.num_elements = 0


    def push(self, data):
        # if stack is empty
        if self.num_elements == 0:
            self.arr = [data]
            self.next_index = 1
            self.num_elements = 1
            return

        # else push old elements in stack and add one
        new_arr = [None] * (self.num_elements+1)

        for i in range(self.num_elements):
            new_arr[i] = self.arr[i]
        new_arr[self.next_index] = data

        self.arr = new_arr
        self.next_index += 1
        self.num_elements += 1
        return


    def pop(self):
         # if stack is empty
        if self.num_elements == 0:
            return None

        new_arr = [None] * (self.num_elements-1)

        for i in range(self.num_elements-1):
            new_arr[i] = self.arr[i]

        popped_data = self.arr[self.num_elements-1]

        self.arr = new_arr
        self.next_index -= 1
        self.num_elements -= 1
        return popped_data


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

    print('Popping data from foo stack: ', foo.pop())
    print('foo array now: ', foo.arr)
