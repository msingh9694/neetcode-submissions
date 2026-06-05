class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        minchar = len(strs[0])
        for ele in strs:
            if len(ele) < minchar:
                minchar = len(ele) 
        
        i = 0
        while i < minchar:
            j = 0
            while j < len(strs)-1:
                if strs[j][i] != strs[j+1][i]:
                    return pre
                j += 1
            i += 1
            
                
            pre += strs[j-1][i-1]

        return pre


        