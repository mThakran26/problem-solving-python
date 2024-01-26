# LeetCode 75 : Find the Difference of Two Arrays
# Question Link : https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75


# Solution : 
def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer1 = list(set(nums1).difference(nums2))
        answer2 = list(set(nums2).difference(nums1))

        answer = [answer1, answer2]
        return answer

