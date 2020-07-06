class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def to_list(self):
        """
        Convert the linked list to normal list
        """
        out_list = []
        node = self.head

        while node:
            out_list.append(node.value)
            node = node.next

        return out_list


    def prepend(self, value):
        """
        Add value to the start of the list
        """
        if self.head is None:
            self.head = Node(value)

        else:
            node = self.head
            self.head = Node(value)
            self.head.next = node
        return


    def append(self, value):
        """
        Add value to the end of the list
        """
        if self.head is None:
            self.head = Node(value)

        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value)
        return


    def search(self, value):
        """
        Search first occurence of the given value
        """
        if self.head is None:
            return None

        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next
        raise ValueError('Value not found')


    def remove(self, value):
        """
        Remove first occurence of given value
        """
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next

        raise ValueError('Value not found in the list')


    def pop(self):
        """
        Return the first node's value and remove it from the list
        """
        if self.head is None:
            return None

        node = self.head
        self.head = node.next

        return node

    def size(self):
        counter = 0
        node = self.head

        while node:
            counter += 1
            node = node.next

        return counter

    def insert(self, value, pos):
        """
        Insert value at pos position in the list.
        If position is larger than the length of the list,
        append to the end of the list.
        """

        # if list is empty
        if self.head is None:
            self.head = Node(value)
            return

        if pos == 0:
            self.prepend(value)

        if pos > self.size():
            self.append(value)
        else:
            index = 0
            node = self.head
            while node.next and index <= pos:
                if (pos - 1) == index:
                    new_node = Node(value)
                    new_node.next = node.next
                    node.next = new_node
                    return

                index += 1
                node = node.next


    def print_list(self):
        """
        Print value of all the nodes of the linked list
        """
        node = self.head
        while node:
            print(node.value)
            node = node.next


# # # # # # # # # # # #
#     Main loop       #
# # # # # # # # # # # #
if __name__ == '__main__':
    # create a linked list
    linked_list = LinkedList()
    linked_list.append(3)
    linked_list.prepend(2)
    linked_list.prepend(1)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.prepend(0)

    # print all the nodes of the linked list
    print('Nodes of linked list:')
    linked_list.print_list()

    # search value
    value = 3
    counter = 0
    search_node = linked_list.head

    while search_node.next:
        counter += 1

        if search_node.value == value:
            break
        search_node = search_node.next

    print('Value {} exits in the linked list at node #{}'.format(value, counter))

    # remove a node and print all the nodes of the new linked list
    linked_list.remove(3)
    print('---- Nodes of new linked list after removing value 3 ----')
    linked_list.print_list()

    # pop first node
    popped_node = linked_list.pop()
    print('---- Linked List after poping first node : {}'.format(popped_node.value))
    linked_list.print_list()

    # size of linked list
    print('Size of given linked list : {}'.format(linked_list.size()))

    # insert node
    #linked_list.insert(3, )
    # linked_list.insert(6, 8)
    print('List after insertion:')
    linked_list.print_list()
