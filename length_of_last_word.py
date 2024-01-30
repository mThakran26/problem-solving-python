# LeetCode Interview 150 : Length of Last Word
# Question Link : https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150

# Solution:
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return (len(words[-1]))