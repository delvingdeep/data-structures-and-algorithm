class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# small linked list
head = Node(1)
head.next = Node(2)

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # move to the tail i.e. last node
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return

    def to_list(self):
        out_list = []
        node = self.head

        while node:
            out_list.append(node.value)
            node = node.next

        return out_list

# create a linked list       
linked_list = LinkedList()
linked_list.append(2)
linked_list.append(5)
linked_list.append(4)
linked_list.append(9)

# print linked list
node = linked_list.head
while node:
    print(node.value)
    node = node.next

# print linked list as list
py_list = linked_list.to_list()
print(py_list)