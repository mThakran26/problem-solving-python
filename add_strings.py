
#Question: 

"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert 
the inputs to integers directly.

"""


# Solution:
def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1)-1
        j = len(num2)-1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                x = int(num1[i])
            else:
                x = 0
            
            if j >= 0:
                y = int(num2[j])
            else:
                y = 0
            
            total = x+y+carry
            carry = total//10
            digit = total%10

            result.append(str(digit))
            i = i-1
            j = j-1
        
        return ''.join(result[::-1])

 