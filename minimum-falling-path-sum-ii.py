from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[0][i] = grid[0][i]

        for i in range(1, n):
            for j in range(n):
                min_pre = 100001
                for jj in range(n):
                    if jj != j:
                        min_pre = dp[i - 1][jj] if min_pre > dp[i - 1][jj] else min_pre

                dp[i][j] = grid[i][j] + min_pre

        return min(dp[-1])
