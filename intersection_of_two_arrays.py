# LeetCode 75 : Intersection Of Two Arrays
# Qestion Link : https://leetcode.com/problems/intersection-of-two-arrays/description/


# Solution :
	def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        comp = nums1+nums2
        for c in comp:
            if c in nums1 and c in nums2:
                res.append(c)

        res = list(set(res))

        return res