# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]] # node, depth
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(depth, max_depth)
                left = node.left
                right = node.right
                stack.append([left, depth + 1])
                stack.append([right, depth + 1])
        
        return max_depth


