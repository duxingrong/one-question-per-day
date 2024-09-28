"""
给出一个区间的集合,请合并所有重叠的区间
intervals=[[1,3],[2,6],[8,10],[15,18]]
输出=[[1,6],[8,10],[15,18]]
"""
from typing import List

class Solution():
    def merge(self,intervals:List[List[int]])->List[List[int]]:
        #左边界排序
        intervals=sorted(intervals,key=lambda x:x[0])
        # 初始化
        space=intervals[0]
        result=[]
        for i in range(1,len(intervals)):
            # 如果左边间大于右边界
            if intervals[i][0]>space[1]:
                result.append(space)
                space=intervals[i]
            else:
                space[1]=max(space[1],intervals[i][1])
        result.append(space)
        return result
            

