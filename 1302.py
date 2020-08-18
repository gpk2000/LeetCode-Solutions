# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root: TreeNode, curr_height: int):
        if not root:
            return
        if curr_height not in self.heights:
            self.heights[curr_height] = list()
        self.heights[curr_height].append(root.val)
        self.solve(root.left, curr_height + 1)
        self.solve(root.right, curr_height + 1)


    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.heights = dict()
        self.solve(root, 0)
        return sum(self.heights[max(self.heights)])
