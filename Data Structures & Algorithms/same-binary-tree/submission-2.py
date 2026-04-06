# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            # bottom out both, can continue to process
            if not node1 and not node2:
                continue
            # one null one not or values not equal
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # add left and right to stack
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))
        
        return True


