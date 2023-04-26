from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        diff_dict = defaultdict(int)
        num_bulls, num_cows = 0, 0

        for char1, char2 in zip(secret, guess):
            if char1 == char2:
                num_bulls += 1
            else:
                if diff_dict[char2] < 0:
                    num_cows += 1

                diff_dict[char2] += 1

                if diff_dict[char1] > 0:
                    num_cows += 1

                diff_dict[char1] -= 1

        return str(num_bulls) + 'A' + str(num_cows) + 'B'
