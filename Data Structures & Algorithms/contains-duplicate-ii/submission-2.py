class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {} # number -> index

        for i, n in enumerate(nums):
            if n in mp and i - mp[n] <= k:
                    return True
            mp[n] = i
        return False