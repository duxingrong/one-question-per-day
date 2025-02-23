"""
218.天际线问题

城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回由这些建筑物形成的天际线。

给个建筑物的几何信息由数组buildings表示，其中三元组buildings[i]=[lefti,righti,height]表示:
lefti是第i座建筑物左边缘的x坐标。
righti是第i座建筑物右边缘的x坐标。
height是第i座建筑物的高度。

你可以假设所有的建筑物都是完美的长方形，在高度为0的绝对平坦的表面上。

天际线应该表示为由'关键点'组成的列表，格式[[x1,y1],[x2,y2],...]，并按x坐标进行排序。关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y坐标始终为0,仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。


高度的变化是天际线的拐点，我们只记录这些拐点。
left事件:建筑开始，可能导致高度升高
right事件:建筑结束，可能导致高度降低
"""

import heapq
from typing import List


class Solution:
    def getSkyline(self,buildings:List[List[int]])->List[List[int]]:
        ## 生成事件点(左端点用负高度，右端点正常)
        events = []
        for left , right , height in buildings:
            events.append((left,-height ,right)) #左端点
            events.append((right,height,None))   #右端点

        ## 排序
        events.sort()

        ## 扫描线+最大堆(加-号间接实现的)
        result = []
        max_heap = [(0,float('inf'))] # 高度+结束位置
        prev_height = 0

        for x , h , right in events:
            if h<0: # 左端点进来
                heapq.heappush(max_heap,(h,right))
            else: # 右端点
                max_heap = [(hh,rr) for hh,rr in max_heap if rr!=x]
                heapq.heapify(max_heap)# 重新排序

            # 维护当前的最大高度 
            curr_height = -max_heap[0][0]

            # 如果高度发生变化，记录关键点
            if curr_height!= prev_height:
                result.append([x,curr_height])
                prev_height = curr_height

        return result
