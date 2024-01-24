#LeetCode-75: Reverse Words in a String
# Question Link : https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75

# Solution:
def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        words = []
        for word in s:
            if word!="":
                words.append(word)

        return ' '.join(words[::-1])