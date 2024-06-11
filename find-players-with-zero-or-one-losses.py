from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {}
        losers = {}
        player_set = set()
        for match in matches:
            winners[match[0]] = winners.get(match[0], 0) + 1
            losers[match[1]] = losers.get(match[1], 0) + 1
            player_set.add(match[0])
            player_set.add(match[1])

        answer_not_lost = []
        answer_one_lost = []
        players = list(player_set)
        players.sort()

        for key in players:

            if winners.get(key) is not None:
                if losers.get(key, 0) == 1:
                    answer_one_lost.append(key)
                elif losers.get(key, 0) == 0:
                    answer_not_lost.append(key)
            elif losers.get(key, 0) == 1:
                answer_one_lost.append(key)

        return [answer_not_lost, answer_one_lost]


print(Solution().findWinners(
    [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))  # [[1], [10]]
