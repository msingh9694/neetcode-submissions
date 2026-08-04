from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count=Counter(s)
        heap=[]
        for ch,frequency in count.items():
            heapq.heappush(heap,(-frequency,ch))
            prev=(0,"")
            res=[]
        while heap:
            frequency,ch=heapq.heappop(heap)
            res.append(ch)
            frequency+=1
            if prev[0]<0:
                heapq.heappush(heap,prev)
            prev=(frequency,ch)
            
        if len(res) != len(s):
            return ""

        return "".join(res)
            
                
            
                
                
            
            
            
            
            
            
            
            
        