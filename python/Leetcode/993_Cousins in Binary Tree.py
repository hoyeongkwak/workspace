'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.
ex1
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

ex2
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

ex3
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
'''
# Definition for a binary tree node.
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        dep = 0
        queue = collections.deque()
        queue.append((root, dep))
        dist = {}
        while queue:
            node, depth = queue.popleft()
            if node.left:
                dist[node.left.val] = (node.val, depth+1)
                queue.append((node.left, depth+1))
            if node.right:
                dist[node.right.val] = (node.val, depth+1)
                queue.append((node.right, depth+1))
        if x not in dist or y not in dist:
            return False
        x_parent, x_depth = dist[x]
        y_parent, y_depth = dist[y]
        return x_depth == y_depth and x_parent != y_parent
