# Question Link: https://leetcode.com/problems/matrix-diagonal-sum/description/?envType=study-plan-v2&envId=programming-skills

# Solution:
class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        sm = 0
        for i in range(n):
            for j in range(len(mat[i])):
                if i==j or i+j == n-1: # will remove double addition of middle num if n is odd
                    sm += mat[i][j]

        return sm
