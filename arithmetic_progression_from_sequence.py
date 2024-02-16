# Question Link: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/?envType=study-plan-v2&envId=programming-skills

# Solution:
class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        ans = True
        arr.sort()
        n = len(arr)
        diff = arr[1] - arr[0]
        for i in range(1, n):
            if i+1 < n:
                if arr[i+1]-arr[i] != diff:
                    ans = False
                    break
        return ans