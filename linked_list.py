"""
Singly Linked List.
    This will keep the reference of next node.

Doubly Linked List.
    This will keep the reference of next & previous node also.
"""


class SNode(object):

    def __init__(self, item, next=None):
        self.item = item
        self.next = next

sl = SNode('a', SNode('b', SNode('c', SNode('d', SNode('e', SNode('f'))))))
print(sl.next.item)
print(sl.next.next.item)
print(sl.next.next.next.item)
        
