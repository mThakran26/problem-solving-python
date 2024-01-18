# Hackerrank Question Link: https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=true

# Solution : 
def angryProfessor(k, a):
    count = 0
    for t in a:
        if t<=0:
            count+=1
            
    if count < k:
        return "YES"
    else:
        return "NO"
