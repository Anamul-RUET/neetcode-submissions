class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        for i in range(0,len(s)):
            if s[i].isalnum():
                s1+=s[i].lower()

        n=len(s1)//2
        for i in range(0,n):
            if s1[i]!=s1[len(s1)-i-1]:
                return False
        return True