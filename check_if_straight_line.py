# Question Link: https://leetcode.com/problems/check-if-it-is-a-straight-line/description/?envType=study-plan-v2&envId=programming-skills

# Solution:
class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        n = len(coordinates)
        y2 = coordinates[1][1]
        y1 = coordinates[0][1]

        x2 = coordinates[1][0]
        x1 = coordinates[0][0]

        y = (y2 - y1)
        x = (x2 - x1)

        for x3, y3 in coordinates[2:]:
            
            if y*(x3-x1) != x*(y3-y1):
                return False
        
        return True