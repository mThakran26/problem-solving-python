# LeetCode 75 : Faulty Keyboard
# Question Link : https://leetcode.com/problems/faulty-keyboard/description/

# Solution:
def finalString(self, s: str) -> str:
        res = ""
        for char in s:
            if char != 'i':
                res+=char
            else:
                res = res[::-1]

        return res