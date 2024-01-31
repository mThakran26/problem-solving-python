# LeetCode Interview 150: Ransom Note
# Question Link: https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

# Solution :
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for char in ransomNote:
            if char in count:
                count[char]+=1
            else:
                count[char]=1
        result = True
        for key in count.keys():
            if count[key] > magazine.count(key):
                result = False

        return result