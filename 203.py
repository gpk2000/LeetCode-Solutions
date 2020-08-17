# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        newHead = None                              # create a new head
        newTail = newHead                           # a tail node for fast insertion to the end
        while head is not None:                     # iterate until head is None
            if head.val != val:
                if newHead == None:                 # quick check if the head is None
                    newHead = ListNode(head.val)
                    newTail = newHead
                else:
                    newNode = ListNode(head.val)    # create the newNode
                    newTail.next = newNode          # add it to the next of the tail
                    newTail = newNode               # make this newNode as the tail
            now = head
            head = head.next                        # advance the head pointer
            del(now)
        return newHead                              # return the new head
