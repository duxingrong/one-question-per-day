"""
给定两个整数n和k,返回1...n中所有可能的k个数的组合
"""

"""
回溯算法,就相当于一棵树,由递归来代表深度.用for循环来确定宽度(虽然还不是太懂)
回溯的三环:
1. 确定递归的参数和返回值
2. 终止条件
3. 单层的递归逻辑
"""
from typing import List
class Solution():
    def combine(self,n:int,k:int)->List[List[int]]:
        result = []
        self.backtracking(n,k,1,[],result)
        return result
    def backtracking(self,n,k,startindex,path,result):
        # 终止条件
        if len(path)==k:
            result.append(path[:])  # 复制品放进结果里

        # 单层处理逻辑
        for i in range(startindex,n+1): # 左闭右开
            path.append(i)
            self.backtracking(n,k,i+1,path,result)
            path.pop()  # 回溯










