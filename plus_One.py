# LeetCode Interview 150 : Plus One
# Question Link : https://leetcode.com/problems/plus-one/description/?envType=study-plan-v2&envId=top-interview-150 

# Solution: 
class Solution:
    def plusOne(self, digits: list[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits 