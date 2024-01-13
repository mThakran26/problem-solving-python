#Hackerrank Question Link : https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true
# Solution :
def sockMerchant(n, ar):
    d = {}
    count = 0
    for a in ar:
        if a not in d:
            d[a]=1
        else:
            d[a]+=1
        
    for key in d:
        if d[key]>=2:
            pair = d[key]//2
            count = count+pair
    
    
    return count