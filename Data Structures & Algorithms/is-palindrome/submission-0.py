class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for ch in s:
            if ch.isalnum():
                result += ch.lower()    
        for i in range(len(result)//2):
            if result[i]!=result[len(result)-1-i]:
                return False
        return True
        