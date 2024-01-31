# LeetCode Interview 150: Longest Common Prefix
# Question Link : https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150

# Solution:
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        compare = min(strs, key = len)
        prefix = ""
        for i in range(len(compare)):
            count = 0
            for s in strs:
                if compare[i] == s[i]:
                    count+=1
            if count == len(strs):
                prefix+=compare[i]
            else:
                break
        
        return prefix
