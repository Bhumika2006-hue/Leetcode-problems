class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Initial number of ways for n = 1
        # aba: patterns where 1st and 3rd colors are same (e.g., RYR)
        # abc: patterns where all 3 colors are different (e.g., RYG)
        aba = 6
        abc = 6
        
        for i in range(2, n + 1):
            # Calculate next states based on current counts
            # New ABA can be formed from 3*old_aba + 2*old_abc
            # New ABC can be formed from 2*old_aba + 2*old_abc
            next_aba = (3 * aba + 2 * abc) % MOD
            next_abc = (2 * aba + 2 * abc) % MOD
            
            aba, abc = next_aba, next_abc
            
        return (aba + abc) % MOD
        