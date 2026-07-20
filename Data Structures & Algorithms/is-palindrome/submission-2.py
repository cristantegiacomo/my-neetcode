class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringa=[c.lower() for c in s if c.isalnum()]
        if "".join(reversed(stringa)) == "".join(stringa):
            return True
        
        return False