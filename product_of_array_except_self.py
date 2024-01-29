# LeetCode 75 : Product of Array Except Self
# Question Link : https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

# Solution :
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = []
        prefix = [0]*n
        suffix = [0]*n
        prefix[0] = 1
        suffix[-1] = 1

        for i in range(1, n):
            prefix[i] = prefix[i-1]*nums[i-1]

        for j in range(n-2, -1, -1):
            suffix[j] = suffix[j+1]*nums[j+1]
        
        for index in range(n):
            ans = prefix[index]*suffix[index]
            answer.append(ans)

        return answer