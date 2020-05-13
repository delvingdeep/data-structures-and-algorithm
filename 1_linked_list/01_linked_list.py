class Node:
    def __init__(self, value):
        '''
        Node class constructor
        '''
        self.value = value
        self.next = None

    def print_linked_list(self):
        '''
        Print any given linked list
        '''
        current_node = self
    
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next


def create_linked_list(input_list):
    '''
    Create a linked list out of a list
    '''
    head = None
    tail = None
    
    for item in input_list:
        if head is None:
            head = Node(item)
            tail = head
        else:
            tail.next = Node(item)
            tail = tail.next
        
    return head
    

# create a random linked list manually
head = Node(2)
head.next = Node(3)
head.next.next = Node(1)
head.next.next.next = Node(5)

# print the linked list
head.print_linked_list()

# create a linked list from a list
list_variable = [3, 4, 2, 9, 1]

linked_list = create_linked_list(list_variable)

# print new linked_list
print('---Linked list from list----')
linked_list.print_linked_list()