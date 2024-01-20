# Hackerrank Question Link : https://www.hackerrank.com/challenges/append-and-delete/problem?isFullScreen=true

# Solution :
def appendAndDelete(s, t, k):
    common = 0
    for i in range(min(len(s), len(t))):
        if s[i]==t[i]:
            common+=1
        else:
            break
    
    total_op = (len(s) - common) + (len(t) - common)
    
    if (k >= len(s) + len(t)) or (k >= (total_op) and k % 2 == (len(s) + len(t)) % 2):
        return "Yes"
    else:
        return "No"