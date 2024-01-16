# Hackerrank Question Link : https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true

# Solution :
def birthday(s, d, m):
    count = 0
    for i in range(n):
        temp = s[i:i+m]
        if len(temp)==m and sum(temp)==d:
            count+=1
            
    return count