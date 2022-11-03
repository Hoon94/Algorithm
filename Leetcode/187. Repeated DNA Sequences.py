from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequence = set()
        repeated = set()

        for i in range(len(s) - 9):
            cur_seq = s[i:i+10]

            if cur_seq in sequence:
                repeated.add(cur_seq)

            sequence.add(cur_seq)

        return [*repeated]
