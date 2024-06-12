from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[0][i] = matrix[0][i]
        for i in range(1, n):
            for j in range(n):
                dp[i][j] = matrix[i][j] + min(
                    dp[i - 1][j],
                    dp[i - 1][j - 1] if j > 0 else float("inf"),
                    dp[i - 1][j + 1] if j < n - 1 else float("inf"),
                )
        return min(dp[-1])
