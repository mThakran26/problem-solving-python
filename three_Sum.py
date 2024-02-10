# LeetCode Interview 150: 3SUM
# Question Link: https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150
"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets."""


# Solution:

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        n = []
        p = []
        z = []
        for num in nums:
            if num>0:
                p.append(num)
            elif num <0:
                n.append(num)
            else:
                z.append(num)
        N = set(n)
        P = set(p)

        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        if len(z) >= 3:
            res.add((0,0,0))
       
        for i in range(len(n)): # For negative pairs plus a positive of equal value summing to zero
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        
        for i in range(len(p)):# For positive pairs plus a negative of equal value summing to zero
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))
        
        return res
