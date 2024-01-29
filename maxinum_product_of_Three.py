# LeetCode 75 : Maximum Product of Three Numbers
# Question Link : https://leetcode.com/problems/maximum-product-of-three-numbers/description/

# Solution :
class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        mxp = max(nums[0]*nums[1]*nums[n-1], nums[n-1]*nums[n-2]*nums[n-3])
        return mxp