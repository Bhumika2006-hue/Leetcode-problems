class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            if x == 2:
                ans.append(-1)
                continue
            
            # Find the position of the first 0 bit starting from the right
            # after the trailing 1s.
            # Effectively, we want to find the first '0' in the sequence of '1's 
            # at the end of the number.
            
            # Count trailing 1s
            temp = x
            count = 0
            while temp & 1:
                temp >>= 1
                count += 1
            
            # We want to flip the bit at (count - 1) position to 0
            # Example: x = 11 (1011). Trailing 1s = 2. Flip bit at index (2-1) = 1.
            # 1011 -> 1001 (9)
            res = x ^ (1 << (count - 1))
            ans.append(res)
            
        return ans