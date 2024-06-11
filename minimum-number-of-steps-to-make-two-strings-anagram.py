class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict = {}

        count = len(s)

        for e in s:
            if s_dict.get(e) is not None:
                s_dict[e] = s_dict[e] + 1
            else:
                s_dict[e] = 1

        for e in t:
            if s_dict.get(e) is not None and s_dict[e] > 0:
                s_dict[e] = s_dict[e] - 1
                count -= 1

        return count

print(Solution().minSteps("leetcode", "practice"))