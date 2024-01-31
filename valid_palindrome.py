# Leetcode interview 150 :  Valid Palindrome
# Question Link : https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150

# Solution:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = []
        for char in s:
            if char.isalnum():
                p.append(char.lower())
        
        if len(p)==0 or p == p[::-1]:
            return True
        else:
            return False
        