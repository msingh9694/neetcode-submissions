from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        parent = [i for i in range(len(accounts))]
        rank = [1] * len(accounts)

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)

            if px == py:
                return

            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1

        # email -> account index
        email_to_account = {}

        # Connect accounts having common emails
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    union(i, email_to_account[email])
                else:
                    email_to_account[email] = i

        # Group emails according to their root account
        groups = defaultdict(list)

        for email, i in email_to_account.items():
            root = find(i)
            groups[root].append(email)

        # Build answer
        result = []

        for root, emails in groups.items():
            result.append([accounts[root][0]] + sorted(emails))

        return result