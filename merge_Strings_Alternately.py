# Leetcode 75 Question Link : https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

# Solution :
def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        l1 = len(word1)
        l2 = len(word2)
        n = min(l1,l2)

        if l1 > l2:
	        extra = word1[n:]
        elif l2 > l1:
	        extra = word2[n:]

        for i in range(n):
	        result = result+word1[i]+word2[i]

        if l1!=l2:
	        result+=extra


        return result