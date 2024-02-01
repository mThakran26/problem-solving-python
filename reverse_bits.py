# LeetCode interview 150: Reverse Bits
# Question Link : https://leetcode.com/problems/reverse-bits/description/?envType=study-plan-v2&envId=top-interview-150

# Solution:
class Solution:
    def reverseBits(self, n: int) -> int:
        binary_string = bin(n)[2:].zfill(32)
        result = ""
        for i in range(len(binary_string)-1, -1, -1):
            result+=binary_string[i]
        return int(result, 2)