class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value)

    def makeCircular(self):
        if self.head is None:
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = self.head
        return

    def print_to_list(self):
        if self.head is None:
            return

        out_list = []
        node = self.head
        while node:
            out_list.append(node.value)
            node = node.next

        print(out_list)


if __name__ == '__main__':
    # create a circular linked list
    linked_list = CircularLinkedList()
    linked_list.append(1)
    linked_list.append(-2)
    linked_list.append(4)

    # print linked list
    print('Original Linked list: ')
    linked_list.print_to_list()

    # make linked list a circular linked list
    linked_list.makeCircular()

    # print linked list for 5 iterations
    print('---- After making linked list Circular ----')
    node = linked_list.head
    for i in range(5):
        print(node.value)
        node = node.next

