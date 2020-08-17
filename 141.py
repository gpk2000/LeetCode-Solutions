# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        We use two pointers a slow one and fast one. If there is a cycle in the list then the fast one would run ahead of the slow and again touch slow one at some point. We use this analogy to implement the O(1) memory solution. If there is no cycle then the fast pointer would hit none or the cant make any jumps.
        """
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast.next == None or fast.next.next == None:
                return False
           slow = slow.next
            fast = fast.next.next
        return True
