#Hackerrank Question Link : https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true

# Solution:
def countingValleys(steps, path):
    path = list(path)
    level = 0
    valleys = 0
    for step in path:
        if step == "U":
            level+=1
        elif step == "D":
            level-=1
        
        if level == 0 and step == "U":
            valleys+=1
    
    return valleys