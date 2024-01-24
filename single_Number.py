# LeetCode-75 : Single Number

# Question Link: https://leetcode.com/problems/single-number/description/?envType=study-plan-v2&envId=leetcode-75

# Solution:
def singleNumber(self, nums: list[int]) -> int:
        res = {}

        for num in nums:
            if num not in res:
                res[num] = 1
            else:
                res[num]+=1
            
        for num,count in res.items():
            if count == 1:
                return num 

