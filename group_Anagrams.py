# LeetCode Interview 150: Group Anagrams
# Question Link:https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150


# Solution: 
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram = defaultdict(list)
        
        for word in strs:
            group_word = ''.join(sorted(word))
            anagram[group_word].append(word)

        return list(anagram.values())