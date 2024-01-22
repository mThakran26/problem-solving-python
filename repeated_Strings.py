# Hackerrank Question Link : https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true

# Solution :
def repeatedString(s, n):
    s_len = len(s)
    mf = n//s_len
    rem = n % s_len
    count = 0
    
    for char in s:
        if char == 'a':
            count+=1
    
    count = count*mf
    
    for i in range(rem):
        if s[i] == 'a':
            count+=1
    
    return count