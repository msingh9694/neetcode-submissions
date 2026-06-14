class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=[]
        for i in range(len(nums)):
            l.append(nums[(i-k)%len(nums)])
        for i in range(len(nums)):
            nums[i]=l[i]


        