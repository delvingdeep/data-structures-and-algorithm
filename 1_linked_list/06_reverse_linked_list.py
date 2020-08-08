class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
        return

    def append(self, value):
        if self.head is None:
            self.head = Node(value)

        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value)
        return

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])

def reverse(linked_list):

    new_list = LinkedList()
    prev_node = None

    for value in linked_list:
        new_node = Node(value)
        new_node.next = prev_node
        prev_node = new_node

    new_list.head = prev_node

    return new_list


def reverse_2(linked_list):
    """
    Second approach to reverse a linked list
    """
    node_list = []
    for node in linked_list:
        node_list.append(node)

    new_linked_list = LinkedList()
    for item in node_list[::-1]:
        new_linked_list.append(item)

    return new_linked_list


def main():
    linked_list = LinkedList()

    linked_list.append(2)
    linked_list.append(5)
    linked_list.append(7)
    linked_list.append(8)

    print('Original List: ')
    print(repr(linked_list))

    rev_list = reverse(linked_list)
    print('Reverse List: ')
    print(repr(rev_list))

    rev_list2 = reverse_2(linked_list)
    print('Second approach: ')
    print(repr(rev_list2))


if __name__ == '__main__':
    main()
