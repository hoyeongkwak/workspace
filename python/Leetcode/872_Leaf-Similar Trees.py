'''
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

ex1
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

ex2
Input: root1 = [1], root2 = [1]
Output: true

ex3
Input: root1 = [1], root2 = [2]
Output: false

ex4
Input: root1 = [1,2], root2 = [2,2]
Output: true
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def inorder(node, res):
            if not root:
                return
            if node.left == None and node.right == Node:
                res.append(node.val)
            inorder(node.left, res)
            inorder(node.right, res)

            return res
        array1 = inorder(root1, [])
        array2 = inorder(root2, [])

        return array1 == array2

