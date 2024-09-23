"""
给定一个包含重复元素的整数数组nums,返回该数组所有可能的子集(幂集)
解集不能包含重复的子集(每个只能元素只能选一次,但是元素可以重复)
"""



"""
回溯的三步骤:
参数: nums: List[int]
返回: result:List[List[int]]
终止条件可以不用,因为有for循环的(startindex,len(nums))来终止 需要的话就是 if startindex==len(nums): return
单层逻辑
result.append(path)  他放在最前面是为了让他收集到空集[]
for i in range(startindex,len(nums)):
if i>startindex and nums[i]==nums[i-1]   # 这里为了成立,所以nums需要进行排序
path.append(nums[i])
self.backtracking()
path.pop()
"""

from typing import List
class Solution():
    def subsetsWithDup(self,nums:List[int])->List[List[int]]:
        result=[]
        if len(nums)==0:
            return result 
        nums=sorted(nums) #排序
        print(nums)
        self.backtracking(nums,0,[],result)
        return result

    def backtracking(self,nums,startindex,path,result):
        result.append(path[:])
        # 终止条件省略了,没必要
        for i in range(startindex,len(nums)):
            if i>startindex and nums[i]==nums[i-1]:
                continue
            path.append(nums[i])
            self.backtracking(nums,i+1,path,result)
            path.pop()

nums=[1,2,3,4,2]
solution=Solution()
print(f"nums的子集和是{solution.subsetsWithDup(nums)}")
