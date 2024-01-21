# Hackerrank Question Link : https://www.hackerrank.com/challenges/halloween-sale/problem?isFullScreen=true

# Solution : 

def howManyGames(p, d, m, s):
    count = 0
    
    while (s >= p):
        count+=1
        s = s - p
        p = max(p-d, m)
     
    return count