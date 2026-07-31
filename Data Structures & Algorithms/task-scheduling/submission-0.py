class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit time
        #minimize idle time
        #tasks=A,A,A,A
        #O(n*m)
        from collections import Counter
        count = Counter(tasks)
        maxheap=[-cnt for cnt in count.values()] 
       # maxHeap = []

        #for cnt in count.values():
            #maxHeap.append(-cnt)
        heapq.heapify(maxheap)
        time=0
        q=deque() #  pairs of [-cnt,idleTime] 
        while  maxheap or q:
            time+=1
            if maxheap:
                cnt=1+heapq.heappop(maxheap)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time



    
        