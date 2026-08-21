class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        mp = {} # number -> index

        for i, n in enumerate(nums):
            if n in mp:
                if abs(i - mp[n]) <= k:
                    return True
                else:
                    mp[n] = i
            else:
                mp[n] = i
        return False