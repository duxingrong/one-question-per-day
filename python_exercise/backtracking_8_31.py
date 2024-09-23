"""
给定一组不含重复元素的整数数组nums,返回该数组所有可能的子集(幂集) ,解集不能包含重复的子集
"""



"""
回溯的三步骤:
1. 参数: nums:List[int]
2. return result=List[List[int]]
3. 终止条件 叶子节点 if startindex==len(nums): return 事实上可以省略,因为for循环成不成立也是一个终止
4. 单层逻辑 for i in range(startindex,len(nums))path.append(num[i]),result.append(path[:])  进入递归,回溯
"""
from typing import List
class Solution():
    def subsets(self,nums:List[int])->List[List[int]]:
        result=[]
        if len(nums)==0:
            return result
        self.backtracking(nums,0,[],result)
        return result

    def backtracking(self,nums,startindex,path,result):
        result.append(path[:])
        # 终止条件(可以省略)
        # if startindex==len(nums):
        #     return 
        for i in range(startindex,len(nums)):
            path.append(nums[i])
            # result.append(path[:])  放在这里会漏掉空集
            self.backtracking(nums,i+1,path,result)
            path.pop()

nums=[1,2,3]
solution=Solution()
print(f"nums的所有子集有{solution.subsets(nums)}")
