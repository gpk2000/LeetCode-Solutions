# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        newHead = ListNode(head.val)
        newTail = newHead
        head = head.next
        while head is not None:
            if newTail.val != head.val:
                newNode = ListNode(head.val)
                newTail.next = newNode
                newTail = newNode
            head = head.next
        return newHead
