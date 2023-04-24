class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def setNext(self, value):
        self.next = LinkedList(value)


# Problem 1 - Remove Duplicate Node - O(n) time - O (1) space
def removeDuplicatesFromLinkedList(linkedList):
    curr = linkedList

    while curr and curr.next:
        next = curr.next
        if curr.value == next.value:
            curr.next = next.next
        else:
            curr = next
        
    return linkedList

"""
head = LinkedList(1)
head.setNext(1)
head.next.setNext(3)
head.next.next.setNext(4)
head.next.next.next.setNext(4)
head.next.next.next.next.setNext(4)
head.next.next.next.next.next.setNext(5)
head.next.next.next.next.next.next.setNext(6)
head.next.next.next.next.next.next.next.setNext(6)

removeDuplicatesFromLinkedList(head)
"""

# Problem 2 - Middle Node
# Approach 1 - Calculate length and then re-iterate until middle node matches target position
def middleNode(linkedList):
    length = calc_node_length(linkedList)
    return get_nth_node(linkedList, length // 2)

def calc_node_length(node):
    length = 0

    while node:
        length += 1
        node = node.next
    
    return length

def get_nth_node(node, target):
    curr = node
    for _ in range(target):
        curr = curr.next

    return curr

# Approach 2 - Have two pointers, a slow node and a fast node - fast node goes 2x speed during traversal
def middleNode2(linkedList):
    node = linkedList
    fast_node = linkedList

    while fast_node and fast_node.next:
        node = node.next
        fast_node = fast_node.next.next
    
    return node
