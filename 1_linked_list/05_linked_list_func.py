class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out_list = []
        node = self.head

        while node:
            out_list.append(node.value)
            node = node.next

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
        node = self.head

        while node:
            if node.value == value:
                return node
            node = node.next

        return None

    def remove(self, value):
        '''
        Remove first occurence of value
        '''
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
        '''
        Return the first node's value and remove it from the list
        '''
        if self.head is None:
            return None

        node = self.head
        self.head = self.head.next

        return node

# # # # # # # # # # # #
#     Main loop       #
# # # # # # # # # # # #

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

# remove a node and print all the nodes of the new linked list
linked_list.remove(3)
print('---- Nodes of new linked list after removing value 3 ----')
new_node = linked_list.head
while new_node:
    print(new_node.value)
    new_node = new_node.next

# pop first node
linked_list.pop()
print('---- Linked List after poping first node ----')
node = linked_list.head
while node:
    print(node.value)
    node = node.next
