# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            # past leaf, balanced w/ 0 height
            if not node: return [True, 0]

            # get info for left and right of curr node
            l = dfs(node.left)
            r = dfs(node.right)

            # balanced when l and r are balanced and
            # their heights are within 1
            balanced = l[0] and r[0] and abs(l[1] - r[1]) <= 1

            return [balanced, 1 + max(l[1], r[1])]

        
        return dfs(root)[0]



