# Hackerrank Question Link : https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true

# Solution
def pickingNumbers(a):
    result = 0
    for i in a:
        count_first = a.count(i) #Count of first number occurence
        count_second = a.count(i+1) #Count of second number occurence
        sub_arr_len = count_first + count_second
        
        if sub_arr_len > result:
            result = sub_arr_len
    
    return result

# catch is that any such sub array will have just two distinct numbers