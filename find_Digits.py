# Hackerrank Question Link : https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=true

# Solution :
def findDigits(n):
    digits = []
    result = []
    
    for digit in str(n):
        digits.append(int(digit))
        
    for d in digits:
        if d!= 0:
            if (n % d == 0):
                result.append(d)
        
            
    return len(result)