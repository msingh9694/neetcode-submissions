class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count = 0

        for num in nums:
            if num != 0:
                product *= num
            else:
                count += 1

        ans = []

        for num in nums:
            if count > 1:
                ans.append(0)
            elif count == 1:
                if num == 0:
                    ans.append(product)
                else:
                    ans.append(0)
            else:
                ans.append(product // num)

        return ans