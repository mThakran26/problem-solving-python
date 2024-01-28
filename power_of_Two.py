# LeetCode 75: Power Of Two
# Question Link : https://leetcode.com/problems/power-of-two/description/

# Solution :
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        result = False
        for x in range(0, 31):
            if pow(2,x) == n:
                result = True
                break
        
        return result
