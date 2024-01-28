# LeetCode 75: Removing Stars From a String
# Question Link : https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75

# Solution :
class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for char in s:
            if char!= '*':
                ans.append(char)
            elif char == '*' and len(ans)>0:
                ans.pop()

        return ''.join(ans)
