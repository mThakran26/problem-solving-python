# LeetCode Interview 150: Add Binary
# Question Link: https://leetcode.com/problems/add-binary/description/?envType=study-plan-v2&envId=top-interview-150

# Solution:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a, 2)
        int_b = int(b, 2)
        int_sum = int_a + int_b
        return bin(int_sum).replace("0b", "") 