'''
prackode's solution
https://leetcode.com/problems/palindrome-number/
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        n=len(s)
        res=1
        for i in range(n):
            if s[i]!=s[n-i-1]:
                res=0
                break
        if res:
            return True
        return False
