class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        i, j = 0, 0
        m2 = nums2[0] if len2>0 else nums1[0]
        rng = (len1+len2) // 2 + 1

        for _ in range(rng):
            m1 = m2
            if i < len1 and j < len2:
                if nums1[i] <= nums2[j]:
                    m2=nums1[i]
                    i+=1
                else:
                    m2=nums2[j]
                    j+=1
            elif j < len2:
                if nums2[j] >= m2:
                    m2=nums2[j]
                    j+=1
                else:
                    break
            elif i < len1:
                if nums1[i] >= m2:
                    m2=nums1[i]
                    i+=1
                else:
                    break

        if (len1+len2) %2==0:
            return (m1+m2) / 2
        else:
            return m2

# [1,3,99] [2,2,5,11,98]  --> [1,2,2,3,5 ,11,98,99]       6 elem