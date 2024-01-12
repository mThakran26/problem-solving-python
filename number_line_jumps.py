#Hackerrank Question Link : https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true
# Solution:
def kangaroo(x1, v1, x2, v2):
    result = "NO"
    for i in range(10000):
        if ((x1+v1)==(x2+v2)):
            result = "YES"
            break
        x1+=v1
        x2+=v2
    return result