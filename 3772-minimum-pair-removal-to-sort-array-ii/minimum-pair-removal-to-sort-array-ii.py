from heapq import heappush, heappop
from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # Doubly linked list pointers
        prev = list(range(-1, n-1))
        nxt = list(range(1, n+1))
        prev[0] = -1
        nxt[n-1] = -1

        # Active flags
        alive = [True]*n

        # Heap of (sum, left_index)
        heap = []
        for i in range(n-1):
            heappush(heap, (nums[i] + nums[i+1], i))

        # Count inversions (violations of non-decreasing)
        bad = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                bad += 1

        def remove_pair(i):
            """merge i and nxt[i]"""
            nonlocal bad

            j = nxt[i]
            if j == -1 or not alive[i] or not alive[j]:
                return False

            # Fix bad count around i, j
            pi = prev[i]
            nj = nxt[j]

            if pi != -1 and nums[pi] > nums[i]:
                bad -= 1
            if nums[i] > nums[j]:
                bad -= 1
            if nj != -1 and nums[j] > nums[nj]:
                bad -= 1

            # Merge
            nums[i] += nums[j]
            alive[j] = False

            # Link list
            nxt[i] = nj
            if nj != -1:
                prev[nj] = i

            # Recalculate bad around merged node
            if pi != -1 and nums[pi] > nums[i]:
                bad += 1
            if nj != -1 and nums[i] > nums[nj]:
                bad += 1

            # Push new adjacent sums
            if pi != -1:
                heappush(heap, (nums[pi] + nums[i], pi))
            if nj != -1:
                heappush(heap, (nums[i] + nums[nj], i))

            return True

        ops = 0
        while bad > 0:
            # get valid min pair
            while heap:
                s, i = heappop(heap)
                j = nxt[i]
                if j != -1 and alive[i] and alive[j] and nums[i] + nums[j] == s:
                    break
            else:
                break

            remove_pair(i)
            ops += 1

        return ops
