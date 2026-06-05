class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p=[]
        count=0
        for i in range(len(nums)):
            if nums[i] !=val:
                count += 1
                p.append(nums[i])
        for j in range(count):
            nums[j] = p[j]
        return count
            

        