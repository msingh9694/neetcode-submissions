from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        nextAvailable = {}

        time = 0

        while freq:
            time += 1
            best = None

            for task in freq:
                if nextAvailable.get(task, 0) <= time:
                    if best is None or freq[task] > freq[best]:
                        best = task

            if best:
                freq[best] -= 1
                nextAvailable[best] = time + n + 1

                if freq[best] == 0:
                    del freq[best]

        return time