class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            p = l
            pivot = nums[r]

            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l,p-1)
            elif p < k:
                return quickSelect(p+1, r)
            else:
                return nums[p]
        
        return quickSelect(0, len(nums)-1)


# [80, 20, 90, 100, 10, 30, 70, 50] k=3 --> {80}
# quando p = (k=5) significa che a destra di p ci sono len-(k=3) elementi piu grandi di nums[p] e a sinistra (k=5) elementi piu piccoli
# GUARDA PROCEDIMENTO SU ONE NOTE