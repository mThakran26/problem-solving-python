#LeetCode 75 : Move Zeroes
# Question Link : https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

# Solution:
def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1, -1, -1):
	        if nums[i]==0:
		        for j in range(i, n):
			        if (j+1) < n:
				        nums[j] = nums[j+1]

		        nums[-1] = 0
