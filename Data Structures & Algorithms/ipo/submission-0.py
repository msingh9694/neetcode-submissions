class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxprofit=[]
        minCapital=[(c,p) for c,p in zip(capital,profits)]
        heapq.heapify(minCapital)
        for i in range(k):
            while minCapital and  minCapital[0][0]<=w:
                c,p=heapq.heappop(minCapital)
                heapq.heappush(maxprofit,-1*p)
            if not maxprofit:
                break
            w+=-1*heapq.heappop(maxprofit)
        return w

        