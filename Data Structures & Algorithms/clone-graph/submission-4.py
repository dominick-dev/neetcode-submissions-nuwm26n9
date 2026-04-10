"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mp = {} # key:old node val:new node

        def dfs(node):
            # reuse copy
            if node in mp:
                return mp[node]

            # make new copy and add to mp
            new_node = Node(node.val, [])
            mp[node] = new_node
            
            # repeat for each neighbor of node
            for neighbor in node.neighbors:
                mp[node].neighbors.append(dfs(neighbor))
            
            return new_node
        
        return dfs(node) if node else None
        
        