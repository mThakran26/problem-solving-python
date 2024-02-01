# Leetcode Interview 150: Single Number II
# Question Link : https://leetcode.com/problems/single-number-ii/description/?envType=study-plan-v2&envId=top-interview-150

# Solution:
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num] = 1

        for key,value in count.items():
            if value==1:
                return key

