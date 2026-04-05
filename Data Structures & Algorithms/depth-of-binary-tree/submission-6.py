# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        res = 0
        if root: q.append(root)
        
        while q:
            q_len = len(q)
            res += 1
            for i in range(q_len):
                curr = q.popleft()
                if curr:
                    if curr.left: q.append(curr.left)
                    if curr.right: q.append(curr.right)
        
        return res

