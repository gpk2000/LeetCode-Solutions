# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return head
        slow = head     # move one step at a time
        fast = head     # move two steps at a time
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow     # slow will be the middle of the list
