# LeetCode 75 : Number of 1 Bits
# Question Link : https://leetcode.com/problems/number-of-1-bits/description/

# Solution : 
class Solution:
    def hammingWeight(self, n : int) -> int:
        count = 0
        for char in str(bin(n)):
            if char == '1':
                count+=1

        return count
