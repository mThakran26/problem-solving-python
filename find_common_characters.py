# LeetCode 75: Find Common Characters
# Question Link : https://leetcode.com/problems/find-common-characters/description/ 

# Solution :
	def commonChars(self, words: list[str]) -> list[str]:
        res = []
        characters =[]

        for char in words[0]:
            characters.append(char)

        for key in characters:
            count = 0
            for i in range(len(words)):
                word = list(words[i])
                if key in word:
                    count+=1
                    word.remove(key)
                    words[i] = word

            if count==len(words):
                res.append(key)

        return res