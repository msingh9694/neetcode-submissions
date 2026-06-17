class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max1=0
        for i in range(len(prices)):
            for j in  range(i+1,len(prices)):
                max1=max(prices[j]-prices[i],max1)
        return max1
            

        