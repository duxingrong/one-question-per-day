"""

149.直线上最多的点数

给你一个数组points，其中points[i]=[xi,yi]表示X-Y平面上的一个点。求最多有多少个点在同一条直线上。


1. 核心是用哈希表统计斜率，并处理特殊情况(重合点和垂直线)
2. 通过gcd规范斜率，确保斜率表示的唯一性。


"""

from typing import List
from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self,points:List[List[int]])->int:
        # 特殊情况
        if len(points)<=2:
            return len(points)

        # 变量max_count
        max_count = 0

        # 开始计算以每个点为基准时候的最大点数
        for i in range(len(points)):
            slopes = defaultdict(int) # slopes是为了分别统计每个基准点的斜率分布，每条直线只会以一个基准点被记录一次

            duplicate = 1 #统计重合点

            for j in range(i+1,len(points)): 
                dx = points[j][0]-points[i][0]
                dy = points[j][1]-points[i][1]
                if dx==0 and dy==0:
                    duplicate+=1
                    continue
                # 化简斜率
                g = gcd(dx,dy)
                dx //= g
                dy //= g
                # 规范化斜率，确保唯一性
                if dx<0:
                    dx,dy = -dx,-dy
                elif dx ==0: #垂直线，dy统一为正
                    dy = abs(dy)
                slopes[(dx,dy)]+=1

            #当前点的最大点数=斜率最多的点+重合点
            max_count=max(max_count,max(slopes.values(),default=0)+duplicate)

        return max_count



