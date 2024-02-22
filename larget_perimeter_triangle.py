# Question: https://leetcode.com/problems/largest-perimeter-triangle/description/?envType=study-plan-v2&envId=programming-skills

# Solution:
class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        result = 0
        for i in range(n-1, -1, -1):
            if i-2 >= 0:
                if nums[i-2] + nums[i-1] > nums[i]:
                    peri = nums[i-2] + nums[i-1] + nums[i]
                    if peri > result:
                        result = peri

        return result
