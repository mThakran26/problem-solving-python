# Hackerrank Question Link : https://www.hackerrank.com/challenges/save-the-prisoner/problem?isFullScreen=true

# Solution:
def saveThePrisoner(n, m, s):
    rem = (n + m + s - 1) % n
    if rem==0:
        return n
    else:
        return rem
