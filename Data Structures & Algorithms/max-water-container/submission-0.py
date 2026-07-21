class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea=[0]*len(heights)

        for pos in range(len(heights)-1):
            offset=1
            area=offset*min(heights[pos],heights[pos+offset])
            while pos+offset+1<len(heights):
                area_plus=(offset+1)*min(heights[pos],heights[pos+offset+1])
                if area_plus > area:
                    area=area_plus
                offset+=1
            maxArea[pos]=area
        return max(maxArea)
