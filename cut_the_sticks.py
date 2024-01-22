# Hackerrank Question Link : https://www.hackerrank.com/challenges/cut-the-sticks/problem?isFullScreen=true

# Solution :
def cutTheSticks(arr):
    
    answer = []
    while arr:
        n = len(arr)
        count = 0
        cut = min(arr)
        
        for i in range(n):
            arr[i]-=cut
            count+=1
        new_arr = []
        for stick in arr:
            if stick > 0:
                new_arr.append(stick)

        arr = new_arr
        answer.append(count) 
    
    return answer