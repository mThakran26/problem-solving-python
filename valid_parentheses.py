# LeetCode Interview 150 : Valid Parentheses
# Question Link : https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150

# Solution:
class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            if char in brackets:
                result.append(char)
            elif len(result)==0 or char != brackets[result.pop()]:
                return False
        
        return len(result)==0