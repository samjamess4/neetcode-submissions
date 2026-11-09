# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        depth = 0


        def findMaxDepth(node, count):
            nonlocal depth  
            if node is None: 
                return 

            depth = max(depth, count)
    
            findMaxDepth(node.left, count + 1)
            findMaxDepth(node.right, count + 1)

        findMaxDepth(root, 1)

        return depth



        