# LeetCode 75 : Remove Element
# Question Link : https://leetcode.com/problems/remove-element/description/

# Solution:
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n-1, -1, -1):
            if nums[i]==val:
                count+=1
                for j in range(i, n):
                    if j+1 < n:
                        nums[j] = nums[j+1]

        k = n - count
        return k
