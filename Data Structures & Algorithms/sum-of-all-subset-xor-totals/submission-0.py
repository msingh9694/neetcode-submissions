class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def helper(nums,index,XORSum):
            if index>=len(nums):
                return XORSum
            including=helper(nums,index+1,XORSum^nums[index])
            excluding=helper(nums,index+1,XORSum)
            return including+excluding
        return helper(nums,0,0)