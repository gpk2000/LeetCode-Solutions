# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curNode = head
        binary_string = ''
        while curNode is not None:
            binary_string += str(curNode.val)
            curNode = curNode.next
        return int(binary_string, 2)
