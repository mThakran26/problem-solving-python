# Leetcode Question Link : https://leetcode.com/problems/two-sum/description/

# Solution :
def twoSum(self, nums):
        n = len(nums)
        result = []
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    result.append(i)
                    result.append(j)
                else:
                    continue
                break
           

        return result
        
