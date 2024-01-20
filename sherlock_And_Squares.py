# Hackerrank Question Link : https://www.hackerrank.com/challenges/sherlock-and-squares/problem?isFullScreen=true

# Solution :
def squares(a, b):
    count = 0
    s = int(math.sqrt(a))
    
    while (s*s) <= b:
        if (s*s) >= a:
            count+=1
        s+=1
        
    return count