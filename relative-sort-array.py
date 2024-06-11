from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        diff = {}
        f = {}
        f2 = {}

        for e in arr2:
            f2[e] = f2.get(e, 0) + 1

        for e in arr1:
            f[e] = f.get(e, 0) + 1
            if f2.get(e) is None:
                diff[e] = diff.get(e, 0) + 1

        diff_list = []
        for e in diff:
            for i in range(diff.get(e)):
                diff_list.append(e)
        diff_list.sort()

        rs = []
        for e in arr2:
            if f.get(e) is not None:
                for i in range(f.get(e)):
                    rs.append(e)

        return rs + diff_list


print(Solution().relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))
