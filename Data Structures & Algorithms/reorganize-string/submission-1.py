from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:

        count = Counter(s)

        maxHeap = []

        for ch, freq in count.items():
            heapq.heappush(maxHeap, (-freq, ch))

        prev = (0, "")
        res = []

        while maxHeap:

            freq, ch = heapq.heappop(maxHeap)

            res.append(ch)

            freq += 1

            if prev[0] < 0:
                heapq.heappush(maxHeap, prev)

            prev = (freq, ch)

        if len(res) != len(s):
            return ""

        return "".join(res)