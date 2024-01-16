# Hackerrank Question Link : https://www.hackerrank.com/challenges/strange-advertising/problem?isFullScreen=true

# Solution:
def viralAdvertising(n):
    total_likes = 0
    recipients = 5
    for day in range(1, n+1):
        liked = math.floor(recipients/2)
        recipients = liked*3
        total_likes += liked
    return total_likes