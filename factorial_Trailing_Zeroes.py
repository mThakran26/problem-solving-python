# LeetCode Interview 150: Factorial Trailing Zeroes
# Question Link: https://leetcode.com/problems/factorial-trailing-zeroes/description/?envType=study-plan-v2&envId=top-interview-150

# Solution:
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while (n>=5):
            n = n//5
            count+=n
        
        return count 