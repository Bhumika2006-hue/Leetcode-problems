class Solution:
    def longestBalanced(self, nums):
        n = len(nums)
        ans = 0
        
        for l in range(n):
            even_set = set()
            odd_set = set()
            
            for r in range(l, n):
                if nums[r] % 2 == 0:
                    even_set.add(nums[r])
                else:
                    odd_set.add(nums[r])
                
                if len(even_set) == len(odd_set):
                    ans = max(ans, r - l + 1)
        
        return ans
