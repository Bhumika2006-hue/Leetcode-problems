class Solution:
    def isTrionic(self, nums):
        n = len(nums)
        i = 0
        
        # 1️⃣ strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0:
            return False
        
        # 2️⃣ strictly decreasing
        j = i
        while j + 1 < n and nums[j] > nums[j + 1]:
            j += 1
        if j == i or j == n - 1:   # 🔥 key fix
            return False
        
        # 3️⃣ strictly increasing again
        while j + 1 < n and nums[j] < nums[j + 1]:
            j += 1
        
        return j == n - 1
