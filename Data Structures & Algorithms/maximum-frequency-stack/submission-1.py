class FreqStack:

    def __init__(self):
        self.p = {}
        self.stack = []

    def push(self, val: int) -> None:
        if val in self.p:
            self.p[val] += 1
        else:
            self.p[val] = 1

        self.stack.append(val)

    def pop(self) -> int:
        # Find the maximum frequency
        max_freq = max(self.p.values())

        # Traverse from the end to get the most recent element
        for i in range(len(self.stack) - 1, -1, -1):
            if self.p[self.stack[i]] == max_freq:
                val = self.stack.pop(i)
                self.p[val] -= 1

                if self.p[val] == 0:
                    del self.p[val]

                return val