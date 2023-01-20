from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self._top = None

    def push(self, x: int) -> None:
        self.q2.append(x)
        self._top = x

        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        result = self.q1.popleft()

        if self.q1:
            self._top = self.q1[0]

        return result

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        return len(self.q1) == 0
