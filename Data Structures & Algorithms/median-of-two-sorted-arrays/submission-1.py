class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        right = len(nums)
        if right % 2 == 1:
            return nums[right // 2]
        else:
            return (nums[right // 2 - 1] + nums[right // 2]) / 2

        