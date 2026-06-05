class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        p=[]
        for i in range(len(strs)):
            if strs[i] != "5":
                g=[strs[i]]
                for j in range(i+1,len(strs)):
                    if sorted(strs[i])==sorted(strs[j]):
                        
                        g.append(strs[j])
                        strs[j] = "5"
                p.append(g)
        return p
                    
                

            


        