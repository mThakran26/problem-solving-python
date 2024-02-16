# Question Link: https://leetcode.com/problems/sign-of-the-product-of-an-array/description/?envType=study-plan-v2&envId=programming-skills

# Solution:
class Solution:
    def arraySign(self, nums: list[int]) -> int:
        product = 1
        for i in range(0, len(nums)):
            if nums[i]==0:
                return 0
            else:
                product*=1 if nums[i] >0 else -1
        return product
