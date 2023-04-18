from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        lookup = Counter(secret)
        x, y = 0, 0

        for i in range(len(guess)):
            if secret[i] == guess[i]:
                x += 1
                lookup[secret[i]] -= 1

        for i in range(len(guess)):
            if guess[i] in lookup and secret[i] != guess[i] and lookup[guess[i]] > 0:
                y += 1
                lookup[guess[i]] -= 1

        return "{}A{}B".format(x, y)
