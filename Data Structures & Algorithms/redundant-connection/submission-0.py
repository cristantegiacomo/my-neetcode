class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)   # rank corrisponde a quanti dipendenti contiene quel nodo (si potrebbe chiamare employees)

        def find(n):    # Path Compression (modifica diretta per risparmiare tempo se chiami di nuovo find per lo stesso numero)
            if parent[n] != n:
                parent[n] = find(parent[n]) 
            return parent[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False    # cycle detected

            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True


        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]