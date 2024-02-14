# Question: 
"""The array-form of an integer num is an array representing its digits in left to right order.
For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k. """

# Solution:
class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:

        for i in range(len(num)-1, -1, -1):
            total = num[i]+k
            num[i] = total%10
            k = total//10
        
        while k > 0:
            digit = k % 10
            k = k // 10
            num.insert(0, digit)
        
        return num