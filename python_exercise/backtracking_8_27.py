"""
给定一个无重复元素的数组candidates和一个目标数target,找出candidates中所有可以使数字和为target的组合(一个数字可以取多次)
"""


"""
回溯三步
参数: candidates, target 
返回: result
终止条件
1. 如果sum(path)==target: result.append(path[:]) return 
2. 如果sum(path) > target: return 剪枝

单层循环逻辑
for i in candidates[startindex:]:
"""
from typing import List
class Solution():
    def combinationSum(self,candidates:List[int],target:int)->List[List[int]]:
        result = []
        if len(candidates)==0:
            return result
        self.traversal(candidates,target,0,[],result)
        return result
    def traversal(self,candidates,target,startindex,path,result):
        # 终止条件
        if sum(path)>target:
            return 
        if sum(path)==target:
            result.append(path.copy())

        #单层逻辑
        for i in range(startindex,len(candidates)):
            val = candidates[i]
            path.append(val)
            # 这次可以取包括他自己和他后面的数字,所以传入的是i,不是i+1
            self.traversal(candidates,target,i,path,result)
            path.pop()

num = [2,3,6,7]
target = 7
solution=Solution()
print(f"所有的组合为{solution.combinationSum(num,target)}")

