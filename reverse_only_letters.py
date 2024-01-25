# LeetCode 75 : Reverse Only Letters
# Question Link : https://leetcode.com/problems/reverse-only-letters/description/

# Solution :
def reverseOnlyLetters(self, s: str) -> str:
        letters = []
        for char in s:
	        if ord(char) in range(97, 123) or ord(char) in range(65, 91):
		        letters.append(char)

        s = list(s)

        for i in range(len(s)):
	        if ord(s[i]) in range(97, 123) or ord(s[i]) in range(65, 91):
		        s[i] = letters[-1]
		        letters.pop()   

        return ''.join(s)
