class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp={}

        for i, n in enumerate(numbers):
            mp[n]=i+1

        for i, n in enumerate(numbers):
            diff=target-n
            if diff in mp and mp[diff]!=i+1:
                return [i+1,mp[diff]]
        return []

# [1, 3, 5, 7, 7, 10, 15, 20] target:8 --> [2,3]