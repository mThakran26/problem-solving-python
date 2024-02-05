# LeetCode interview 150 : Longest Consecutive Sequence
# Question Link: https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150

"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

"""

# Solution:
def longestConsecutive(self, nums: list[int]) -> int:
        n=len(nums)
        nums.sort()
        if n==1:
            return 1
        if n==0:
            return 0
        count=1
        max_count=-1
        for i in range(n-1):
            if nums[i+1]-nums[i]==1: # consecutive
                count+=1
            elif nums[i+1]-nums[i]==0: # they are equal
                max_count=max(max_count,count)
                continue
            else:
                count=1
            max_count=max(max_count,count)
        return max_count


