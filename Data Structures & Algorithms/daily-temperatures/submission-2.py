class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l=len(temperatures)
        res=[0]*l

        for i in range(l-1):
            count=0
            for j in range(i+1, l):
                count+=1
                if temperatures[j]>temperatures[i]:
                    res[i]+=count
                    break
        return res