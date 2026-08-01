class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxprof = 0
        st, stI= prices[0], 0
        end = 0

        for i in range(len(prices)):
            if st != min(st,prices[i]):
                stI=i
                end=0
            st= min(st, prices[i])
            if i > stI:
                end = max(end, prices[i])
                maxprof=max(maxprof, end-st)
        return maxprof


# [10,2,5,1,6,7,1]