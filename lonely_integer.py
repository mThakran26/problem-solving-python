# Hackerrank Question link : https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two

# Solution :
def lonelyinteger(a):
    unique = []
    for num in a:
        if num not in unique:
            unique.append(num)
        else:
            unique.remove(num)
            
    return unique[0]

