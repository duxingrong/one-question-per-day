"""
老师给孩子们分发糖果,有N个孩子站成了一条直线,老师会根据每个孩子的表现,预先给他们评分
分发要求
1. 每个孩子至少分配1个糖果
2. 相邻的孩子中,评分高的孩子必须获得更多的糖果
"""

"""
这里要注意第二点的问题,意思是如果孩子评分高于左边,那他糖果一定要大于左边,如果他的评分高于右边,那他的糖果也一定要大于右边
所以我们需要两次遍历,来保证这个规则在左到右和右到左都成立
"""
from typing import List
class Solution():
    def function(self,ratings:List[int])->int:
        # 用列表来记录每个孩子的糖果数量    
        val=[1]*len(ratings)

        # 和他的左边比较
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                val[i]=val[i-1]+1 # 保证评分高就要糖更多
        # 和他的右边比较
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                val[i]=max(val[i],val[i+1]+1)
        return sum(val)

