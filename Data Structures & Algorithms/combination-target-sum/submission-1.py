class Solution:
    def solve(self,index,total,subset,candidates,target,result):
        if total==target:
            result.append(subset.copy())
            return
        elif total>target:
            return
        if index>=len(candidates):
            return
        summ=total+candidates[index]
        subset.append(candidates[index])
        self.solve(index,summ,subset,candidates,target,result)
        summ=total
        subset.pop()
        self.solve(index+1,summ,subset,candidates,target,result)
        

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        self.solve(0,0,[],nums,target,result)
        return result





        