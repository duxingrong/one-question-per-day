"""
给定一个可包含重复数字的序列nums,按任意顺序返回所有不重复的全排列
"""


"""
这里是返回所有不重复的全排列,不仅是选过的不能再选择,还要进行树层去重(树层去重我们进行排序) 这里的判断条件就是 if used[i] and (i>0 and nums[i]==nums[i-1] and not used[i-1]) 就continue
1. used[i] : 这是因为如果我们path里面有了,自然不能在选择
2. nums[i]==nums[i-1] 说明现在是有重复的了,但是我们允许树枝重复,但不允许树层重复 ,所以如果used[i-1]==True 说明他是上一层的时候被选择的,属于树枝重复,就不管;如果是used[i-1]==False 说明是树层重复 就要跳过.
举例:
[1,2,2] 你第一层递归选择了[1] ,第二层里面你选择第一个2,得[1,2] ,这时候这个used=[True,True,False] ,你这时候当然可以继续选择2,就得了一组排序[1,2,2] ,但是当你回溯重新来到1时候,used=[True,False,False],你选择第二个2,这时候很明显你会重复,这时候你的第一个2的used为False 

*所以(i>0 and nums[i]==nums[i-1] and not used[i-1]) 可以作为树枝去重和树层去重的条件*
"""
from typing import List
class Solution():
    def permuteUnique(self,nums:List[int])->List[List[int]]:
        result = []
        used=[False]*len(nums)
        if len(nums)==0:
            return result
        self.backtracking(nums,used,[],result)
        return result
    
    def backtracking(self,nums,used,path,result):
        # 终止条件
        if len(path)==len(nums):
            result.append(path[:])
            return 
        # 单层逻辑
        for i in range(0,len(nums)):
            if used[i] or (i>0 and nums[i]==nums[i-1] and not used[i-1]):
                continue
            used[i]=True
            path.append(nums[i])
            self.backtracking(nums,used,path,result)
            path.pop()
            used[i]=False


nums=[1,1,2]
solution=Solution()
print(f"所有的不重复排序有{solution.permuteUnique(nums)}")
