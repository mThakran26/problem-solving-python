# LeetCode 75 - Reverse Vowels of a String
# Question Link : https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

#Solution:
def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        s_vowels = []
        for char in s:
            if char in vowels:
                s_vowels.append(char)

        s = list(s)

        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = s_vowels[-1]
                s_vowels.pop()
        