class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head):
        self.head = head


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head

        # Iterate till the end of the LinkedList
        while node.next:
            node = node.next
        node.next = Node(value)

        return


    def to_list(self):
        out_list = []

        if self.head is None:
            return

        node = self.head

        while node:
            out_list.append(node.value)
            node = node.next

        return out_list


def merge(list1, list2):

    if list1 is None:
        return list2

    if list2 is None:
        return list1

    list_1 = list1.to_list()
    list_2 = list2.to_list()

    merged_list = sorted(list_1 + list_2)

    merged_linked_list = LinkedList(None)

    for value in merged_list:
        merged_linked_list.append(value)

    return merged_linked_list


class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)

    def _flatten(self, node):

        # termination condition
        if node.next is None:
            return merge(None, node.value)

        # _flatten() is calling itself until a termination condition is achieved
        return merge(self._flatten(node.next), node.value)


if __name__ == '__main__':

    # create first linked list
    first_linked_list = LinkedList(Node(1))
    first_linked_list.append(3)
    first_linked_list.append(5)

    print('First Linked List: ', first_linked_list.to_list())

    # create second linked list
    second_linked_list = LinkedList(Node(2))
    second_linked_list.append(4)

    print('Second Linked List: ', second_linked_list.to_list())

    # merge both the linked list first and second
    merged_list = merge(first_linked_list, second_linked_list)
    print('--- After merging both linked list ---')
    print(merged_list.to_list())

    # create a nested linked list
    print('--- Creating nested linked list ---')
    nested_linked_list = NestedLinkedList(Node(first_linked_list))
    nested_linked_list.append(second_linked_list)

    # flatten the nested linked list
    flattened_linked_list = nested_linked_list.flatten()
    print('Flattened nested linked list: ', flattened_linked_list.to_list())



