class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            node = self.head
            while node:
                node = node.next
            node = Node(value)
        return


    def create_linked_list(self, arr):
        if len(arr) == 0:
            return

        self.head = Node(arr[0])

        node = self.head
        for num in arr[1:]:
            node.next = Node(num)
            node = node.next
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


    def even_after_odd(self):
        if self.head is None:
            return

        # odd linked list
        odd_head = None
        odd_tail = None

        # even linked list
        even_head = None
        even_tail = None

        current_node = self.head

        while current_node:
            next_node = current_node.next

            # node is odd
            if current_node.value % 2 == 1:
                # if node is empty, append at head
                if odd_head is None:
                    odd_head = current_node
                    odd_tail = odd_head
                else:
                    # append node at the tail
                    odd_tail.next = current_node
                    odd_tail = odd_tail.next

            # node is even
            else:
                if even_head is None:
                    # if node is empty, append at head
                    even_head = current_node
                    even_tail = even_head
                else:
                    even_tail.next = current_node
                    even_tail = even_tail.next
            current_node.next = None
            current_node = next_node


        if odd_head is None:
            return even_head

        if even_head is None:
            return odd_head

        odd_tail.next = even_head

        return odd_head


if __name__ == '__main__':

    arr1 = [1, 2, 3, 4, 5, 6]
    arr2 = [1, 3, 5, 7]
    arr3 = [2, 4, 6, 8]

    linked_list = LinkedList()
    linked_list.create_linked_list(arr1)
    linked_list.print_to_list()

    print('--- Applying even after odd ----')


    
