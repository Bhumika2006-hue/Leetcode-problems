class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0
        
        # Helper function to check if array is non-decreasing
        def is_sorted(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True

        # Simulation loop
        while not is_sorted(nums):
            min_sum = float('inf')
            target_idx = -1
            
            # 1. Find the leftmost pair with the minimum sum
            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i+1]
                if current_sum < min_sum:
                    min_sum = current_sum
                    target_idx = i
            
            # 2. Replace the pair with their sum
            # nums[target_idx] becomes the sum, then we remove the next element
            nums[target_idx] = min_sum
            nums.pop(target_idx + 1)
            
            operations += 1
            
        return operations