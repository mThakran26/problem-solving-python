# Question: https://leetcode.com/problems/capitalize-the-title/description/

# Solution:
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        for i in range(len(words)):
            if len(words[i]) <= 2:
                words[i] = words[i].lower()
            else:
                first = (words[i][0]).upper()
                rest = ""
                for j in range(1,len(words[i])):
                    rest += words[i][j].lower()
                words[i] = first+rest

        return " ".join(words) 
                