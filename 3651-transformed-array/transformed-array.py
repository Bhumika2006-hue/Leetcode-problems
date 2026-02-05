class Solution:
    def constructTransformedArray(self, nums):
        n = len(nums)
        result = [0] * n
        
        for i in range(n):
            if nums[i] > 0:
                result[i] = nums[(i + nums[i]) % n]
            elif nums[i] < 0:
                result[i] = nums[(i + nums[i]) % n]  # nums[i] is negative
            else:
                result[i] = 0
        
        return result
