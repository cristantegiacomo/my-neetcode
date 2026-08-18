class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        size = len(needle)
        l = 0
        r = size-1

        while r < len(haystack):
            while r < len(haystack) and haystack[l] != needle[0]:
                l += 1
                r += 1
            if haystack[l:r+1] == needle:
                return l
            l += 1
            r += 1

        return -1