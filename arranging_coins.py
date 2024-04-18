#Question: https://leetcode.com/problems/arranging-coins/description/?envType=study-plan-v2&envId=binary-search

# Solution:
class Solution:
    def arrangeCoins(self, n: int) -> int:
        stair_count = 0

        for i in range(1,n):
            if i<=n:
                stair_count+=1
                n = n-i

            else:
                break

        if stair_count==0:
            return 1
        else:
            return stair_count
