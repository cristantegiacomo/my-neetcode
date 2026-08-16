"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        q = deque([node])
        mp = {}
        mp[node] = Node(node.val)
        

        while q:
            curr = q.popleft()
            for nbr in curr.neighbors:
                if nbr not in mp:
                    q.append(nbr)
                    mp[nbr] = Node(nbr.val)
                mp[curr].neighbors.append(mp[nbr])
        
        return mp[node]