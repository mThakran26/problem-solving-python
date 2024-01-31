# LeetCode Interview 150 : Repeated Substring Pattern
# Question Link : https://leetcode.com/problems/repeated-substring-pattern/description/

# Solution :
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        substr = ""
        result = False

        for i in range(0, int(n/2)):
            substr+=s[i]
            m = int(n / len(substr))
            comp = substr*m
            if comp == s:
                result = True
                break
            else:
                continue
        
        return result
