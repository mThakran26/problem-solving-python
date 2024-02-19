# Question: https://leetcode.com/problems/baseball-game/description/?envType=study-plan-v2&envId=programming-skills

# Solution:
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for i in operations:
            if i=="C":
                stack.pop()
            elif i=="D":
                stack.append(2*stack[-1])
            elif i=="+":
                sm=stack[-2]+stack[-1]
                stack.append(sm)
            else:
                stack.append(int(i))
        return sum(stack)