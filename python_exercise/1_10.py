"""
给出集合[1,2,3,...,n]，其所有元素共有n!种排列

按大小顺序列出所有排列情况，并一一标记

给定n和k，返回第k个排列

关键是换个角度思考，从暴力的解法中抽离出来，找到隐藏的数字规律
抓住排列的结构性规律:
集合[1,2,...,n]的排列是有规律的，每个数字开头的排列数目有(n-1)!个，通过k的值可以直接判断到哪一组，确定了第一个数字后，将这个数字排除并且更新k的值，就可以递归下去，而不用生成所有的对列！
"""

from math import factorial


class Solution:
    def getPermutation(self,n:int,k:int)->str:

        nums = list(range(1,n+1))
        result = []

        k = k-1 #化成0索引

        for i in range(n): ## 这里遍历n次，是因为我们一共要取n次，每一次result+一个数字
            ## 当前组的长度
            fact = factorial(n-1-i)
            index = k//fact
            result.append(str(nums[index]))
            nums.pop(index)
            k = k%fact

        return "".join(result)
            

if __name__ == "__main__":
    solution = Solution()
    print(solution.getPermutation(4,8))
        

