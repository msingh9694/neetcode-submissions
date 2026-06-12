class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = []

        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    l.append(i + 1)
                    l.append(j + 1)
                    return l

        return l