# Hackerrank Question Link: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?isFullScreen=true

#Solution:
def catAndMouse(x, y, z):
    
    cat_A = abs(z - x)
    cat_B = abs(y - z)
    
    if cat_A < cat_B:
        result = "Cat A"
    elif cat_B < cat_A:
        result = "Cat B"
    elif cat_A==cat_B:
        result = "Mouse C"
    
    return result
