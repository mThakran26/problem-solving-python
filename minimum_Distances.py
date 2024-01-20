# Hackerrank question Link : https://www.hackerrank.com/challenges/minimum-distances/problem?isFullScreen=true

# Solution :
def minimumDistances(a):
    d = []
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            if a[i]==a[j]:
                d.append(abs(i-j))
    
    if len(d) > 0:
        return min(d)
    else:
        return -1