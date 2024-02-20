# Question: https://leetcode.com/problems/robot-return-to-origin/description/?envType=study-plan-v2&envId=programming-skills

# Solution (Brute Force): 
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0

        for m in moves:
            if m == "U":
                y+=1
            elif m == "D":
                y-=1
            elif m == "L":
                x-=1
            elif m == "R":
                x+=1

        if x ==0 and y == 0:
            return True
        else:
            return False
                
# Solution (optimized):
class Solution:
    def judgeCircle(self, moves: str) -> bool:     
        if moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R"):
            return True
        else:
            return False