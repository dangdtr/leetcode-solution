from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        f = {}
        for e in arr:
            f[e] = f.get(e, 0) + 1

        return len(set(f.values())) == len(f.values())