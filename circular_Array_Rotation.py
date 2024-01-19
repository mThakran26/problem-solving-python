# Hackerrank Question Link : https://www.hackerrank.com/challenges/circular-array-rotation/problem?isFullScreen=true

# Solution :
def circularArrayRotation(a, k, queries):
    result = []
    k = k % n
    a[:] = a[-k:] + a[:-k]
    
    for query in queries:
        result.append(a[query])
        
    return result
