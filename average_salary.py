# Question Link: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/?envType=study-plan-v2&envId=programming-skills

# Solution:
class Solution:
    def average(self, salary: list[int]) -> float:
        n = len(salary)
        salary.sort()
        total = sum(salary[1:n-1])
        return total/(n-2)