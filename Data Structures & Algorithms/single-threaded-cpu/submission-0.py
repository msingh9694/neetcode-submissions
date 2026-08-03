from heapq import heappush, heappop

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        n = len(tasks)

        # (enqueueTime, processingTime, index)
        tasks = sorted(
            [(e, p, i) for i, (e, p) in enumerate(tasks)]
        )

        waiting = []

        ans = []

        time = 0

        i = 0

        while i < n or waiting:

            # CPU idle
            if not waiting:
                time = max(time, tasks[i][0])

            # Add all available tasks
            while i < n and tasks[i][0] <= time:

                e, p, idx = tasks[i]

                heappush(waiting, (p, idx))

                i += 1

            # Execute shortest task
            p, idx = heappop(waiting)

            time += p

            ans.append(idx)

        return ans