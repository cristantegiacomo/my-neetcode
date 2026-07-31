class Solution:
    def search(self, nums: List[int], target: int) -> int:
# [5,6,7,8,0,1,2,3,4]       

        l, r = 0, len(nums)-1

        while l <= r:
            m = l + (r-l) // 2

            if target >= nums[l]:
                if nums[m] >= nums[l]:
                    if nums[m] > target:
                        r = m - 1
                    elif nums[m] < target:
                        l = m + 1
                    else:
                        return m
                else:
                    r = m - 1
            else:
                if nums[m] < nums[l]:
                    if nums[m] > target:
                        r = m - 1
                    elif nums[m] < target:
                        l = m + 1
                    else:
                        return m
                else:
                    l = m + 1

        return -1