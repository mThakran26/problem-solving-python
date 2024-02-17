# Question: Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

# Solution:
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd_count = (high - low)//2
    
        if (high % 2 != 0 or low % 2 != 0): # if either R or L is odd, one more added to count
            odd_count+= 1
    
        return odd_count
