# LeetCode Interview 150 : Best Time to Buy and Sell Stock II
# Question Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150

# Solution:
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        if not prices or len(prices) < 2:
            return 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
