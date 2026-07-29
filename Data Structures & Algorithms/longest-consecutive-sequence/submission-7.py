class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        seen=set(nums)

        for n in nums:
            if n-1 not in seen:
                length=0
                while (n+length) in seen:
                    length+=1
                longest=max(longest,length)
        return longest

