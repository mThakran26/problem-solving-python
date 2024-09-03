"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def twoSum(nums, target):
        result = [0,0]
        n = len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    result[0] = i
                    result[1] = j
                    break
                else:
                    continue
        return result


nums = [2,7,11,15]
target = 9

print(twoSum(nums,target))