class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        p={}
        res=[]
        perm=[]
        for i in nums:
            if i in p:
                p[i]+=1
            else:
                p[i]=1
        def dfs():
            if len(perm)==len(nums):
                res.append(perm.copy())
                return
            for n in p:
                if p[n] > 0:
                    perm.append(n)
                    p[n] -= 1

                    dfs()
                    p[n] += 1
                    perm.pop()

                
        dfs()
        return res
        
        