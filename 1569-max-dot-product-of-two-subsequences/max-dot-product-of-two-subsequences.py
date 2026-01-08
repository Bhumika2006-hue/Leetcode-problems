class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        # Initialize DP table with negative infinity
        # dp[i][j] represents max dot product using nums1[:i] and nums2[:j]
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # Calculate the product of current pair
                current_product = nums1[i-1] * nums2[j-1]
                
                # Option 1: Current product + best result from previous subsequences
                # Option 2: Just current product (starting a new subsequence)
                # Option 3: Skip current element of nums1
                # Option 4: Skip current element of nums2
                dp[i][j] = max(
                    current_product, 
                    current_product + max(0, dp[i-1][j-1]),
                    dp[i-1][j],
                    dp[i][j-1]
                )
        
        return dp[n][m]
        