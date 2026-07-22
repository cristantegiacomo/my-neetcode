class Solution:
    def minOperations(self, s: str) -> int:
        count=0     #s[0]=0     01010101...

        for i, c in enumerate(s):
            if i %2==0: 
                if c=='1': count+=1
            else:
                if c=='0': count+=1
        return min(count,len(s)-count)


