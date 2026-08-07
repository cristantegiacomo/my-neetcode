class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        last = m + n - 1
        valid = m - 1
        j = i = k = 0

        while j < n:
            if valid-i >= 0 and nums1[valid-i] > nums2[n-1]:
                nums1[last-k] = nums1[valid-i]
                i += 1
            else:
                nums1[last-k] = nums2[n-1]
                n -= 1
            k+=1
        return nums1 