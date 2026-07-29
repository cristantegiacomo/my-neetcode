class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_ord = sorted(set(nums))
        lung = 1
        n_lung = 1

        if len(nums)==0:
            return 0

        for i in range(len(nums_ord) - 1):
            if nums_ord[i] == nums_ord[i+1]-1:
                n_lung += 1
                if i==len(nums_ord)-2:
                    lung=max(lung,n_lung)
            else:
                lung=max(lung,n_lung)
                n_lung = 1
        return lung
