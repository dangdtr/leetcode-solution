from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        f = {}
        for e in nums:
           f[e] = f.get(e, 0) + 1

        colors = [0, 1, 2]
        idx = 0
        for c in colors:
            if c in f:
                for i in range(f[c]):
                    nums[idx] = c
                    idx += 1
