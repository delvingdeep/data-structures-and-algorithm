class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out_list = []
        current = self.head

        while current:
            out_list.append(current.value)
            current = current.next

        return out_list

    def prepend(self, value):
        previous_head = self.head
        self.head = Node(value)
        self.head.next = previous_head
        return

    def append(self, value):
        if self.head is None:
            self.head = Node(value)

        else:
            node = self.head
            while node:
                node = node.next
                if node.next is None:
                    node.next = Node(value)
                    break
        return

    def search(self, value):
        current = self.head

        while current:
            if current.value == value:
                return current
            current = current.next

        return None

    # def remove(self, value):
    #     '''
    #     Remove first occurence of value
    #     '''
    #     current = self.head
    #
    #     while current:
    #         if current.value == value:
    #             continue
    #         new_ll.next = Node(current.value)
    #         current = current.next
    #         new_ll = new_ll.next
    #
    #     return new_ll



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
list_node = linked_list.head
while list_node:
    print(list_node.value)
    list_node = list_node.next

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

# # remove a node and print all the nodes of the new linked list
# new_list = linked_list.remove(3)
# print('Nodes of new linked list:')
# new_node = new_list.head
# while new_node:
#     print(new_node.value)
#     new_node = new_node.next
