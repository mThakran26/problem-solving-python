# Question: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/?envType=study-plan-v2&envId=binary-search

# Solution:
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        result = [-1, -1]
        count = 0 #to check occurence...whether only one or more than 1. First occurence will remain fixed while last would change.
        for i in range(len(nums)):
            if nums[i] == target:
                count+=1
                if count==1:
                    result[0] = i
                    result[1] = i
                if count > 1:
                    result[1] = i
                    
        return result