# Hackerrank Question Link : https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true

# Solution:
def migratoryBirds(arr):
    
    seen_count_dict = {}
    result = []
    for a in arr:
        if a in seen_count_dict:
            seen_count_dict[a]+=1
        else:
            seen_count_dict[a] =1
            
    max_count = max(seen_count_dict.values())
    for key, value in seen_count_dict.items():
        if value == max_count:
            result.append(key)
    
    return min(result)