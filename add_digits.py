# Question: Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# Solution: 
class Solution:
    def addDigits(self, num: int) -> int:
        while num >=10: 					# Below 10 only single digit numbers(0-9) 
            digits = list(str(num))
            num = sum(map(int, digits)) 
        return num
        

