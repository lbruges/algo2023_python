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