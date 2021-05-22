# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ret = 0
        def dfs(self, node, L, R):
            if not node:
                return
            if L <= node.val <= R:
               ret

        return