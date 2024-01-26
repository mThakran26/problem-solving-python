# Hackerrank Question Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two

# Solution:
def diagonalDifference(arr):
    pd =[]
    sd =[]
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n):
            if i==j:
                pd.append(arr[i][j])
            if i+j == n-1:
                sd.append(arr[i][j])
    
    return abs(sum(sd)-sum(pd))