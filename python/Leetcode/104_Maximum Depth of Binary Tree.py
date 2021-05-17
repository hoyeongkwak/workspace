# Definition for a binary tree node.
'''
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

ex1
Input: root = [3,9,20,null,null,15,7]
Output: 3

ex2
Input: root = [1,null,2]
Output: 2

ex3
Input: root = []
Output: 0

ex4
Input: root = [0]
Output: 1
'''
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return
        queue = deque()
        depth = 1
        queue.append((root, 1))
        while queue:
            node, height = queue.popleft()
            depth = max(depth, height)
            if node.left is not None:
                queue.append((node.left, height + 1))
            if node.right is not None:
                queue.append((node.right, height + 1))
        return depth
