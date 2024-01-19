# Hackerrank Question Link: https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true

# Soultion:
def utopianTree(n):
    if n==0:
        h = 1
    elif n > 0:
        h = 1
        for cycle in range(1, n+1):
            if cycle% 2 == 0:
                h = h+1
            else:
                h = h*2
    
    
    return h
