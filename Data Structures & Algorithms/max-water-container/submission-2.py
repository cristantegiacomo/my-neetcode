class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0

        for pos in range(len(heights)-1):
            for offset in range(1, len(heights)-pos ):
                area=(offset)*min(heights[pos],heights[pos+offset])
                max_area=max(area, max_area)
        return max_area

#miglioramento scrittura del codice