# Question Link: https://leetcode.com/problems/find-smallest-letter-greater-than-target/?envType=study-plan-v2&envId=binary-search

# Solution: 
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        result = "{"
        for letter in letters:
            if ord(letter) > ord(target):
                result = min(result, letter)
        if result == "{":
            return letters[0]
        else:
            return result