# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = deque()
        q.append(root)

        while q:
            q_len = len(q)
            rightmost = None

            for i in range(q_len):
                curr = q.popleft()
                if curr:
                    rightmost = curr
                    q.append(curr.left)
                    q.append(curr.right)
            if rightmost: res.append(rightmost.val)

        return res


        # array of nodes in each level
        # return array of last node in each level
        