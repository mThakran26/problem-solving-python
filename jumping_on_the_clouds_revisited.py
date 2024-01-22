# Hackerrank Question Link : https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem?isFullScreen=true

# Solution :
def jumpingOnClouds(c, k):
    e = 100
    n = len(c)
    i = 0
    while True:
        if c[i] == 1:
            e = e - 2    
        e = e - 1
        i = (i+k)%n
        if i == 0:
            break
            
    return e