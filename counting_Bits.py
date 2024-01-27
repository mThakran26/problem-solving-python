# LeetCode 75 : Counting Bits
# Question Link : https://leetcode.com/problems/counting-bits/description/?envType=study-plan-v2&envId=leetcode-75

# Solution:
class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = []
        for i in range(n+1):
            b_val = list(bin(i))
            count = b_val.count('1')
            ans.append(count)

        return ans