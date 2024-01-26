# Hackerrank Question Link : https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

# Solution :
def timeConversion(s):
    h = s[0:2]
    m = s[8:10]
    time = ""
    
    if m == "AM":
        if h == "12":
            h = "00"
            
    elif m == "PM":
        if h != "12":
            h = int(h)+12
          
    time = str(h)+s[2:8]
    return time