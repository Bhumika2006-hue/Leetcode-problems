import bisect
from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums, k, dist):
        n = len(nums)
        need = k - 1

        small = SortedList()
        large = SortedList()
        small_sum = 0

        def add(x):
            nonlocal small_sum
            if len(small) < need:
                small.add(x)
                small_sum += x
            else:
                if x < small[-1]:
                    y = small.pop()
                    small_sum -= y
                    large.add(y)
                    small.add(x)
                    small_sum += x
                else:
                    large.add(x)

        def remove(x):
            nonlocal small_sum
            if x in small:
                small.remove(x)
                small_sum -= x
                if large:
                    y = large.pop(0)
                    small.add(y)
                    small_sum += y
            else:
                large.remove(x)

        ans = float('inf')

        # initialize first window
        for i in range(1, dist + 2):
            add(nums[i])

        if len(small) == need:
            ans = small_sum

        # slide window
        for l in range(2, n - dist):
            remove(nums[l - 1])
            add(nums[l + dist])
            if len(small) == need:
                ans = min(ans, small_sum)

        return nums[0] + ans
