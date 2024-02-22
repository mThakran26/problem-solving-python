# Question Link: https://leetcode.com/problems/contains-duplicate/description/

# Solution:
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            elif num in d :
                d[num]+=1
                if d[num] == 2:
                    return True
                
        return False


