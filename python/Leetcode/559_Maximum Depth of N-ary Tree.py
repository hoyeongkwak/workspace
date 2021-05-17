'''
Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

ex1
Input: root = [1,null,3,2,4,null,5,6]
Output: 3

ex2
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5
'''

from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return
        #queue = collections.deque()
        queue = deque()
        depth = 1
        queue.append((root, depth))
        while queue:
            node, dep = queue.popleft()
            if node.children:
                for child in node.children:
                    queue.append((child, dep+1))
