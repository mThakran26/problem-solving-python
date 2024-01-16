# Hackerrank Question Link : https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true

# Solution :
def climbingLeaderboard(ranked, player):
    ranked = sorted(list(set(ranked)), reverse=True)
    player = sorted(player, reverse=True)
    
    r = len(ranked)
    p = len(player)
    j=0
    result = []
    
    for i in range(p):
        while j<r and player[i]<ranked[j]:
            j+=1
        
        result.append(j+1)
        
    return result[::-1]