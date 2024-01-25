# Hackerrank Question Link : https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

# Solution :
def miniMaxSum(arr):
    total = sum(arr)
    mn = total - max(arr)
    mx = total - min(arr)
    
    print(f"{mn} {mx}")