class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        return

    def print_list(self):
        if self.head is None:
            return None

        node = self.head
        while node:
            print(node.value)
            node = node.next


    def isCircular(self):
        """
        Determine whether the Linked List is circular or not

        Args:
            linked_list(obj): Linked List to be checked
        Returns:
            bool: Return True if the linked list is circular, return False otherwise
        """
        if self.head is None:
            return False

        slow = self.head
        fast = self.head

        while fast and fast.next:
            # slow pointer moves one node
            slow = slow.next

            # fast pointer moves two nodes
            fast = fast.next.next

            if slow == fast:
                return True

        return False


def main():

    # create linked list
    list_values = [3, 5, 19, 34, 2]
    linked_list = LinkedList(list_values)
    linked_list.append(4)

    print('Linked List: ')
    linked_list.print_list()

    # creating a loop where tail points to second node
    print('--- Creating a loop by connecting tail to second node ---')
    loop_start = linked_list.head.next
    node = linked_list.head
    while node.next:
        node = node.next
    node.next = loop_start

    print('Is loop circular? : ', linked_list.isCircular())




if __name__ == '__main__':
    main()
