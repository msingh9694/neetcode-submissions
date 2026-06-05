class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre=""
        minstr=len(strs[0])
        if len(strs)==1:
            return strs[0]
        for ele in strs:
            if len(ele)<=minstr:
                minstr=len(ele)
        for i in range(minstr):
            for j in range(1,len(strs)):
                if strs[j-1][i] != strs[j][i]:
                    return pre
            else:
                pre+=strs[j][i]
        return pre
        