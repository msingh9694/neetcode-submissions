class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()

            y = stones.pop()
            x = stones.pop()

            if y != x:
                stones.append(y - x)

        if stones:
            return stones[0]
        else:
            return 0