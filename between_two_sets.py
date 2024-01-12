#Hackerrank_Question_link: https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true
#Question:

"""There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

1.The elements of the first array are all factors of the integer being considered
2.The integer being considered is a factor of all elements of the second array

These numbers are referred to as being between the two arrays. Determine how many such numbers exist.
"""



# Solution  :
def getTotalX(a, b):
    x1 = a[0]
    x2 = b[-1]
    result = []
    
    for x in range(x1, x2+1):
        res_a = res_b = "Yes"
        for i in a:
            if (x% i) != 0:
                res_a = "No"

        for j in b:
            if (j% x) != 0:
                res_b = "No"

        if res_a == "Yes" and res_b == "Yes":
            result.append(x)

    return len(result)