"""
给定一个没有重复数字的序列,返回所有可能的全排列
"""


"""
这里的区别就是,每一次递归的时候,你的选项不再是由startindex来划分,而是只要是path里没有的元素,都是你递归时要遍历的,这里就需要用一个新的方法: 使用一个全局变量used=[False]*len(nums) ,来进行遍历的取舍,而每次遍历都会遍历全部的元素
"""

from typing import List
class Solution():
    def permute(self,nums:List[int])->List[List[int]]:
        result=[]
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
            if used[i]==True:
                continue
            path.append(nums[i])
            used[i]=True
            self.backtracking(nums,used,path,result)
            path.pop()
            used[i]=False

nums=[1,2,3]
solution=Solution()
print(f"所有的排序方式有{solution.permute(nums)}")



