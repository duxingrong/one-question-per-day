"""
给定一个整型数组,任务是找到所有的该数组的递增子序列,递增子序列的长度至少为2
这题最大的难点在于你没办法进行排序,因为求的就是原始数组的所有递增子序列,这样的话我们*树层去重*只能用哈希表或者set()
"""



"""
回溯的三步骤:
参数: List[int]
返回: List[List[int]]
终止条件  startindex=len(nums) 可以没有,因为for循环的(startindex,len(nums)) 会自动终止
单层逻辑:
if len(path)>1 : result.append(path[:])
这里需要用used=set()来记录本层中哪些使用过,然后进行剪枝
for 循环 如果 (path[-1]<nums[i] and nums[i] not in used)  
used.append(nums[i])
path.append(nums[i])
self.backtracking()
path.pop()
"""
from typing import List
class Solution():
    def findSubsequences(self,nums:List[int])->List[List[int]]:
        result = []
        if len(nums)==0:
            return result
        self.backtracking(nums,0,[],result)
        return result

    def backtracking(self,nums,startindex,path,result):

        # 终止条件直接舍去
        # 添加结果
        if len(path)>1: 
            result.append(path[:])
        # 单层逻辑
        used=set()
        for i in range(startindex,len(nums)):
            if (path and path[-1]>nums[i]) or nums[i]  in used:  # 得path有值才能保证path[-1]有意义
                continue
            used.add(nums[i])
            path.append(nums[i])
            self.backtracking(nums,i+1,path,result)
            path.pop()

nums=[4,6,7,7]
solution=Solution()
result=solution.findSubsequences(nums)
print(result)
