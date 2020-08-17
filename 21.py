# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newHead = None                      # initialize newHead
        newTail = None                      # and newTail for fast append
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:             # l2 is small
                newNode = ListNode(l2.val)  # so append l2.val at the end
                if newHead is None:         # quick check if head is None
                    newHead = newNode
                    newTail = newHead
                else:
                    newTail.next = newNode
                    newTail = newNode
                l2 = l2.next                # increment the l2 to its next
            else:                           # l1 is small
                newNode = ListNode(l1.val)  # so append l1.val at the end
                if newHead is None:         # quick check if head is None
                    newHead = newNode
                    newTail = newHead
                else:
                    newTail.next = newNode
                    newTail = newNode
                l1 = l1.next                # increment the l1 to its next

        # copy the remaining elements left in l1
        while l1 is not None:
            newNode = ListNode(l1.val)
            if newHead is None:             # quick check if head is None
                newHead = newNode
                newTail = newHead
            else:
                newTail.next = newNode
                newTail = newNode
            l1 = l1.next

        # copy the remaining elements left in l2
        while l2 is not None:
            newNode = ListNode(l2.val)
            if newHead is None:             # quick check if head is None
                newHead = newNode
                newTail = newHead
            else:
                newTail.next = newNode
                newTail = newNode
            l2 = l2.next

        # return the newHead
        return newHead
