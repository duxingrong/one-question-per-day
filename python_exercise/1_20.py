"""

135.分发糖果

n个孩子占成一排。给你一个整数数组ratings表示每个孩子的评分。

你需要按照以下要求，给这些孩子分发糖果:
- 每个孩子至少分配到一个糖果
- 相邻两个孩子评分更高的孩子会获得更多的糖果

请你给每个孩子分发糖果，计算并返回需要准备的最少糖果数目。

"""
from typing import List
class Solution:
    def candy(self,ratings:List[int])->int:

        n = len(ratings)

        candys = [1]*n

        # 处理左遍历
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                candys[i]=candys[i-1]+1

        # 处理右边规则
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candys[i] = max(candys[i],candys[i+1]+1) # 这里需要这样做来省塘

        return sum(candys)

        

