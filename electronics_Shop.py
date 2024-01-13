#Hackerrank Question Link : https://www.hackerrank.com/challenges/electronics-shop/problem?isFullScreen=true

#Solution:
def getMoneySpent(keyboards, drives, b):
    result = []
    for k in keyboards:
        for d in drives:
            if k+d <= b:
                result.append(k+d)
            
    if len(result)!= 0:
        return max(result)
    else:
        return -1