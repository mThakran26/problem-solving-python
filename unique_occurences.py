# LeetCode 75 : Unique Number of Occurences
# Question Link : https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75

# Solution Link : 
def uniqueOccurrences(self, arr: list[int]) -> bool:
        occ_dict = {}
        for a in arr:
            if a not in occ_dict:
                occ_dict[a] = 1
            else:
                occ_dict[a]+=1

        occ = list(occ_dict.values())
        occ_set = set(occ_dict.values())

        if len(occ) == len(occ_set):
            return True
        else:
            return False