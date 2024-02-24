# Question Link: https://leetcode.com/problems/richest-customer-wealth/description/?envType=study-plan-v2&envId=programming-skills

# Solution:
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for cust_acc in accounts:
            wealth = sum(cust_acc)
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth
        