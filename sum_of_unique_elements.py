# Question Link: https://leetcode.com/problems/sum-of-unique-elements/description/

# Solution:
class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        num_counts = {}
        sm = 0
        for num in nums:
            if num in num_counts:
                if num_counts[num] == 1:
                    sm -= num
                num_counts[num] += 1
            else:
                num_counts[num] = 1
                sm += num
        return sm

