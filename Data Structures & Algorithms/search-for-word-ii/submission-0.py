from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False

    def addword(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.isword = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Create Trie root
        root = TrieNode()

        # Insert all words into Trie
        for w in words:
            root.addword(w)

        ROWS, COLS = len(board), len(board[0])

        res = set()
        visit = set()

        def dfs(r, c, node, word):

            # Boundary + visited + Trie check
            if (
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or
                board[r][c] not in node.children
            ):
                return

            visit.add((r, c))

            # Move to next Trie node
            node = node.children[board[r][c]]

            # Add current character
            word += board[r][c]

            # Complete word found
            if node.isword:
                res.add(word)

            # Explore 4 directions
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            # Backtrack
            visit.remove((r, c))

        # Start DFS from every cell
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)