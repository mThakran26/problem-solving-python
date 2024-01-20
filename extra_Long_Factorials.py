# Hackerrank Question Link : https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=true

# Solution :
def extraLongFactorials(n):
    for i in range(n-1, 1, -1):
        n *= i   
    print(n)

