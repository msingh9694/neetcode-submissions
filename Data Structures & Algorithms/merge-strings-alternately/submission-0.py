class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        temp = ""

        for i in range(min(len(word1), len(word2))):
            temp += word1[i]
            temp += word2[i]

        temp += word1[len(word2):]
        temp += word2[len(word1):]

        return temp