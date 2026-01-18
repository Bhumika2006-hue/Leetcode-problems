from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Prefix sums
        rowSum = [[0] * (n + 1) for _ in range(m)]
        colSum = [[0] * n for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                rowSum[i][j + 1] = rowSum[i][j] + grid[i][j]
                colSum[i + 1][j] = colSum[i][j] + grid[i][j]

        def getRowSum(r, c1, c2):
            return rowSum[r][c2] - rowSum[r][c1]

        def getColSum(c, r1, r2):
            return colSum[r2][c] - colSum[r1][c]

        maxSize = min(m, n)

        for k in range(maxSize, 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    target = getRowSum(i, j, j + k)

                    valid = True

                    # Check rows
                    for r in range(i, i + k):
                        if getRowSum(r, j, j + k) != target:
                            valid = False
                            break

                    if not valid:
                        continue

                    # Check columns
                    for c in range(j, j + k):
                        if getColSum(c, i, i + k) != target:
                            valid = False
                            break

                    if not valid:
                        continue

                    # Diagonals
                    diag1 = diag2 = 0
                    for d in range(k):
                        diag1 += grid[i + d][j + d]
                        diag2 += grid[i + d][j + k - 1 - d]

                    if diag1 == target and diag2 == target:
                        return k

        return 1
