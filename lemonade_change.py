# Question Link: https://leetcode.com/problems/lemonade-change/description/?envType=study-plan-v2&envId=programming-skills

# Solution:
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        wallet = {5 :0 , 10 : 0} # We cannot return 20 so not keeping in change wallet
        for bill in bills:
            if bill==5:
                wallet[5]+=1
            elif bill == 10 and wallet[5] >= 1:
                wallet[10]+=1
                wallet[5]-=1
            elif bill == 20 and wallet[5]>=1 and wallet[10]>=1:
                wallet[5]-=1
                wallet[10]-=1
            elif bill == 20 and wallet[5] >= 3:
                wallet[5]-=3    
            else:
                return False

        return True  