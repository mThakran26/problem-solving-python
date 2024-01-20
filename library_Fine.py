# Hackerrank Question Link : https://www.hackerrank.com/challenges/library-fine/problem?isFullScreen=true

# Solution :
def libraryFine(d1, m1, y1, d2, m2, y2):
    fine = 0
    if y1==y2:
        if m1==m2:
            if d1 > d2:
                fine = 15*(d1-d2)
            else:
                fine = 0
    
        else:
            if m1 > m2:
                fine = 500*(m1-m2)
    elif y1 > y2:
        fine = 10000
        
    return fine