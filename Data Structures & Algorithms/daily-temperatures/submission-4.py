class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l=len(temperatures)
        res=[0]*l

        for i in range(l-1):
            for j in range(i+1, l):
                if temperatures[j]>temperatures[i]:
                    res[i]=j-i
                    break
        return res
        
# soluzione O(n) senza usare count ma usando gli indici j-i