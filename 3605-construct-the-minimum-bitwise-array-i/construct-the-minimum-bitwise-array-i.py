from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for p in nums:
            # Even numbers are impossible
            if p % 2 == 0:
                ans.append(-1)
                continue

            found = -1
            # Try smallest possible x
            for x in range(p):
                if (x | (x + 1)) == p:
                    found = x
                    break

            ans.append(found)

        return ans
