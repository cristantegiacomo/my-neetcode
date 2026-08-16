"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        mp = {}

        def dfs(node):
            if node in mp:
                return mp[node]
                
            cpy = Node(node.val)
            mp[node] = cpy

            for nbr in node.neighbors:
                mp[node].neighbors.append(dfs(nbr))

            return cpy

        return dfs(node) if node else None