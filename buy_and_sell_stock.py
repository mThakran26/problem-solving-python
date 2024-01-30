# LeetCode Interview 150 : Best Time to Buy and Sell Stock
# Question Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150

# Solution:
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy = prices[0]
        for price in prices[1:]:
            buy = min(buy, price)
            profit = max(profit, price - buy)

        return profit 
