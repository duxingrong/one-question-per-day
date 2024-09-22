"""
给定一个仅包含数字2-9的字符串,返回所有它能表示的字母组合
2:abc
3:def
4:ghi
5:jkl
6:mno
7:pqrs
8:tuv
9:wxyz
"""

"""
回溯算法
用字典来连接数字和他的字符串
每一次递归终止都会得到一个字符串(path),然后将他放进result 的条件是索引(index)= 长度(digits) --因为这说明已经遍历完了
"""
from typing import List
class Solution():
    def __init__(self):
        self.dict ={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"

        }
    def letterCombinations(self,digits:str)->List[List[str]]:
        # 特殊情况
        result = []
        if len(digits)==0:
            return result
        self.traversal(digits,0,"",result)
        return result
    def traversal(self,digits,index,path,result):
        # 终止条件
        if index == len(digits):
            result.append(path)   # 在python中,字符串是不可变的,path+char会产生一个新的字符串,而不是原来的path,所以不需要用复制体
            return 

        # 单层逻辑
        for char in self.dict[digits[index]]:
            self.traversal(digits,index+1,path+char,result)  # python可以直接字符串相加

# 测试
solution = Solution()
print(solution.letterCombinations("23"))















