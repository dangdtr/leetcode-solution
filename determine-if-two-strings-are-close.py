def counter(word) -> dict:
    count = {}
    for c in word:
        count[c] = count.get(c, 0) + 1
    return count


class Solution:

    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        count1 = counter(word1)
        count2 = counter(word2)
        return sorted(count1.values()) == sorted(count2.values()) and set(count1.keys()) == set(count2.keys())