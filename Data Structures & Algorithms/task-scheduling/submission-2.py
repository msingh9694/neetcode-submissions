from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxFreq = max(count.values())

        maxCount = 0

        for value in count.values():
            if value == maxFreq:
                maxCount += 1

        return max(len(tasks), (maxFreq - 1) * (n + 1) + maxCount)