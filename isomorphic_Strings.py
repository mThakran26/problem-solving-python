# LeetCode Interview 150: ISOMORPHIC STRINGS
# Question Link: https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150
"""Question: 
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself."""


#Solution:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        i=0
        for char in s:
            if char not in s_dict:
                s_dict[char]=i
                i+=1
        j=0
        for char in t:
            if char not in t_dict:
                t_dict[char]=j
                j+=1

        result = True
        for k in range(len(s)):
            if s_dict[s[k]] != t_dict[t[k]]:
                result = False
        return result


