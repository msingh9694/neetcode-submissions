class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = list(range(len(accounts)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Map email -> account index
        email_to_account = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    parent[find(i)] = find(email_to_account[email])
                else:
                    email_to_account[email] = i

        # Group emails by their root account
        merged = {}

        for email, i in email_to_account.items():
            root = find(i)
            merged.setdefault(root, []).append(email)

        # Build result
        result = []

        for root, emails in merged.items():
            result.append([accounts[root][0]] + sorted(emails))

        return result