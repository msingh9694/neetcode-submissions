class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        while left<=right:
            mid=(left+right)//2
            count=0
            rd=1
            for ele in weights:
                if count+ele>mid:
                    rd+=1
                    count=0
                count+=ele
            if rd<=days:
                right=mid-1
            else:
                left=mid+1
        return left

        