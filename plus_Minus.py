# Hackerrank Question Link : https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

# Solution ;
def plusMinus(arr):
    
    positive = []
    negative = []
    zero = []
    
    for num in arr:
        if num > 0:
            positive.append(num)
        elif num < 0:
            negative.append(num)
        elif num == 0:
            zero.append(num)
            
    print( (len(positive)/(len(arr))))
    print( (len(negative)/(len(arr))))
    print( (len(zero)/(len(arr))))