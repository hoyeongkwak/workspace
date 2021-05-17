'''
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

ex1
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

ex2
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

Treenode : [10,5,15,3,7,null,18]
low : 7
high : 15

result = 32
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ret = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        '''
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return an
        '''
        self.dfs(root, low, high)
        return self.ret

    def dfs(self, node, L, R):
        if not node:
            return

        if L <= node.val <= R:
            self.ret += node.val
            self.dfs(node.left, L, R)
            self.dfs(node.right, L, R)
        elif node.val > R:
            self.dfs(node.left, L , R)
        else:
            self.dfs(node.right, L, R)
