"""1) Create a singly linked list and implement append (add to end) and print_list (print all nodes) methods."""


class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val       # stores the node's value
        self.next = next     # pointer to next node, None by default

    def __str__(self):
        return str(self.val) # allows printing node directly as its value

def print_list(head):
    curr = head
    elements = []
    while curr:                          # traverse until end of list
        elements.append(str(curr.val))   # collect each node's value
        curr = curr.next                 # move to next node
    print(' -> '.join(elements))         # print all values with arrow separator

def insert_at_end(head, val):
    curr = head
    while curr:
        if curr.next == None:            # found the last node
            curr.next = SinglyNode(val)  # attach new node at the end
            break
        curr = curr.next                 # move forward

"""head = SinglyNode(1)       # create head node with value 1
insert_at_end(head, 2)     # append 2
insert_at_end(head, 3)     # append 3
print_list(head)           # print entire list  """ 

"""2) Given a linked list, delete a node with a given value."""

def remove_val(head, val):
    prev = None      # tracks the node before curr
    curr = head      # start traversal from head
    while curr:
        if curr.val == val:          # found the node to delete
            if prev is None:         # deleting the head node
                head = curr.next     # move head to next node
            else:
                prev.next = curr.next  # skip over curr, linking prev to curr's next
            break                    # node removed, stop traversal
        prev = curr                  # move prev forward
        curr = curr.next             # move curr forward
    return head                      # return head in case it changed

"""3) Given a linked list, reverse it in-place."""

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next = curr.next    # save next before overwriting
        curr.next = prev    # reverse the pointer
        prev = curr         # move prev forward
        curr = next         # move curr forward
    return prev

"""head = SinglyNode(1)
insert_at_end(head, 2)
insert_at_end(head, 3)
insert_at_end(head, 6)
print_list(head)

head = reverse_list(head)
print_list(head)"""

"""4) Create a doubly linked list and implement append and prepend (add to front) methods."""

class Doublynode:
    def __init__(self, val, next=None, prev=None):
        self.val = val       # stores the node's value
        self.next = next     # pointer to next node
        self.prev = prev     # pointer to previous node

    def __str__(self):
        return str(self.val) # allows printing node directly as its value

def display_double(head):
    elements_double = []
    curr = head
    while curr:                                # traverse until end of list
        elements_double.append(str(curr.val))  # collect each node's value
        curr = curr.next                       # move forward
    print(' <-> '.join(elements_double))       # print with double arrow separator

def append_list(head, val):
    curr = head
    while curr:
        if curr.next is None:                # found the last node
            new_node = Doublynode(val)       # create new node
            curr.next = new_node             # link last node forward to new node
            new_node.prev = curr   
            break          # link new node backward to last node
    return head                              # head unchanged

def prepend_list(head, val):
    new_node = Doublynode(val)               # create new node
    new_node.next = head                     # new node points forward to old head
    head.prev = new_node                     # old head points back to new node
    return new_node                          # new node is the new head

"""head = Doublynode(1)

head = append_list(head, 2)
display_double(head)

head = prepend_list(head, 4)
display_double(head)"""
    
"""5) Given a doubly linked list, delete a node with a given value."""      

def remove_list(head, val):
    prev = None              # tracks node before curr
    curr = head              # start traversal from head
    while curr:
        if curr.val == val:              # found the node to delete
            if prev is None:             # deleting the head node
                head = curr.next         # move head forward
                if head:                 # if new head exists
                    head.prev = None     # clear its backward pointer
            else:
                prev.next = curr.next    # skip over curr going forward
                if curr.next:            # if next node exists
                    curr.next.prev = prev  # update its backward pointer
            break                        # node removed, stop traversal
        prev = curr                      # move prev forward
        curr = curr.next                 # move curr forward
    return head                          # return head in case it changed

"""head = Doublynode(1)

head = append_list(head, 2)
display_double(head)

head = prepend_list(head, 4)
display_double(head)

head = remove_list(head, 4)
display_double(head)"""
