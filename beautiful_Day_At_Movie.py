# Hackerrank Question Link : https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true
 # Solution:
 def beautifulDays(i, j, k):
    beautiful_day_count = 0
    
    for num in range(i, j+1):
        reverse = int(str(num)[::-1])
        diff = abs(num - reverse)
        
        if diff % k == 0:
            beautiful_day_count+=1
        
    return beautiful_day_count