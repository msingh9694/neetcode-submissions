class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left=max(nums)
        right=sum(nums)
        while left<=right:
            mid=(left+right)//2
            count = 1
            current_sum = 0

            for element in nums:
                if current_sum + element > mid:
                    count += 1
                    current_sum = element
                else:
                    current_sum += element
            if count<=k:
                right=mid-1
            else:
                left=mid+1
        return left
                


        