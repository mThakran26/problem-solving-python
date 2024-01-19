# Hackerrank Question Link : https://www.hackerrank.com/challenges/the-hurdle-race/problem?isFullScreen=true

# Solution:

def hurdleRace(k, height):
    
    hurdle_threshold = max(height)
    
    if k >= hurdle_threshold:
        return 0
    else:
        return hurdle_threshold-k
     
