
from typing import List

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True

        if 1 in nums:
            return False

        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return

            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            size[root_a] += size[root_b]

        # Map each prime factor to the first index containing it.
        prime_owner = {}

        for i, num in enumerate(nums):
            d = 2

            while d * d <= num:
                if num % d == 0:
                    if d in prime_owner:
                        union(i, prime_owner[d])
                    else:
                        prime_owner[d] = i

                    while num % d == 0:
                        num //= d

                d += 1

            # Any remaining factor greater than 1 is prime.
            if num > 1:
                if num in prime_owner:
                    union(i, prime_owner[num])
                else:
                    prime_owner[num] = i

        root = find(0)

        for i in range(1, n):
            if find(i) != root:
                return False

        return True
