class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 1
        seen = set()
        longest = 1

        if len(s)==0:
            return 0

        seen.add(s[0])
        while r < len(s):
            if s[r] in seen:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l+=1
                seen.remove(s[l])
                l+=1
            longest = max(longest, r-l+1)
            seen.add(s[r])
            r+=1
        return longest
  #      A1ZCR1T7