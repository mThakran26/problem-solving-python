# Hackerrank Question Link : https://www.hackerrank.com/challenges/service-lane/problem?isFullScreen=true
# Solution:
def serviceLane(n, cases):
    result = []
    for c in range(t):
        i = cases[c][0]
        j = cases[c][1]
        widths = []
        for index in range(i, j+1):
            widths.append(width[index])
        w = min(widths)
        result.append(w)
        
    return result