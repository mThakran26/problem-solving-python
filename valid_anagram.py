# LeetCode Interview 150: VALID ANAGRAM
# Question Link: https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters
exactly once.

"""

# Solution:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        if len(s) != len(t):
            return False
        else:
            for char in s:
                if char not in s_dict:
                    s_dict[char]=1
                else:
                    s_dict[char]+=1

            for char in t:
                if char not in t_dict:
                    t_dict[char] = 1
                else:
                    t_dict[char]+=1

            for key,value in s_dict.items():
                if key in t_dict and value == t_dict[key]:
                    continue
                else:
                    return False
                    break
            return True




