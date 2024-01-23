# LeetCode-75 Question Link : https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75
# 1431. Kids With the Greatest Number of Candies

# Solution :
def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        greatest = max(candies)
        print(greatest)
        for candy in candies:
            if candy + extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)

        return result