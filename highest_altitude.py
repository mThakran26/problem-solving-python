# LeetCode 75 : Find the Highest Altitude
# Question Link : https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75

#Solution:
def largestAltitude(self, gain: list[int]) -> int:
        n = len(gain)
        altitudes = [0]
        alt = 0
        for i in range(0, n):
	        alt = alt+gain[i]
	        altitudes.append(alt)

        return max(altitudes)