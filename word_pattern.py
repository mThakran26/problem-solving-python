# LeetCode Interview 150: Word pattern
# Question Link: https://leetcode.com/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150

# Solution:
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        p_dict = {}
        w_dict = {}

        if len(pattern) != len(words):
            return False

        i=0
        for char in pattern:
            if char not in p_dict:
                p_dict[char] = i
                i+=1

        j = 0 
        for word in words:
            if word not in w_dict:
                w_dict[word] = j
                j+=1

        result = True
        for k in range(len(pattern)):
            p = pattern[k]
            w = words[k]
            if p_dict[p] != w_dict[w]:
                result = False

        return result