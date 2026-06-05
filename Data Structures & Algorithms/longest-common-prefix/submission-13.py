class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre=""
        index = 0
        if len(strs) == 1:
            return strs[0]
        for i in strs:
            ans = min(100000,len(i))
        while index < ans:
            for i in range(len(strs)-1):
                if index < len(strs[i]) and index < len(strs[i+1]):
                    if strs[i][index] != strs[i+1][index]:
                        return pre
                else:
                    return pre
           
            pre += strs[i][index]
            index += 1
        return pre

    
                    
                
        

        

        