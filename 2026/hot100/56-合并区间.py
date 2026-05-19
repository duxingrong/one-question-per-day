"""
56. 合并区间

以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 


输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6]


"""

"""
区间问题，优先考虑排序；合并区间，排序后只看当前的区间能否和结果数组最后一个区间是否重叠
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # 按照左端点排序
        intervals.sort(key=lambda x: x[0])

        ans = [] # 结果数组

        for interval in intervals:

            # 刚开始直接加入
            if not ans : 
                ans.append(interval)

            # 判断当前数组开头和结果数组最后一个的右端点的大小
            if interval[0] <= ans[-1][1]: 
                ans[-1][1] = max(ans[-1][1],interval[1])

            else: # 没有重叠，也是直接加入
                ans.append(interval)

        return ans 
