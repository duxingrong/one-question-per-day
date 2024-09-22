"""
找出所有相加之和为n的k个数的组合,组合中只允许含有1-9的正整数,并且每种组合中不存在重复的数字
"""

"""
回溯算法
参数: n,k,startindex,result,path
返回值: result

最底层的逻辑:
如果 sum(path)==n,result.append(path[:])  return 

#单层的处理逻辑:
for 循环,中途一路加i ,再进入递归,出来时path.pop()   i的区间[startindex,9-(k-len(path))+1+1]:其中9-还需要的长度+1就得到了i最大的起始位置
其中+1 是为了下标对齐 ,然后再加一是为了range左闭右开
"""

from typing import List
class Solution():
    def combinationSum3(self,k:int,n:int)->List[List[int]]:
        result = []
        self.traversal(n,k,1,[],result)
        return result
    
    def traversal(self,n,k,startindex,path,result):
        # 终止条件
        if sum(path)>n:  # 剪枝
            return 
        if len(path)==k:
            if sum(path)==n:
                result.append(path[:])
            return 
        
        # 单层逻辑
        for i in range(startindex,9-(k-len(path))+2):
            path.append(i)
            self.traversal(n,k,i+1,path,result)
            path.pop()


solution = Solution()
print(solution.combinationSum3(9, 3))

