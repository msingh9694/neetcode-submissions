class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        l = []

        for i in range(len(numbers)):
            need = target - numbers[i]

            if need in seen:
                l.append(seen[need] + 1)
                l.append(i + 1)
                return l

            seen[numbers[i]] = i

        return l