# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sum(self, root: TreeNode):
        child_sum = 0
        if not root:
            return 0
        if root.left is not None:
            child_sum += root.left.val
        if root.right is not None:
            child_sum += root.right.val
        return child_sum

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.val % 2 == 0:
            return self.sum(root.left) + self.sum(root.right) + self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)
        return self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)
