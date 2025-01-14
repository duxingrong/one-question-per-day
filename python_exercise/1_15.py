"""

最大矩形

给定一个仅包含0和1,大小为rows*cols的二维二进制矩阵，找出只包含1的最大矩形，并返回其面积

"""
from typing import List


class Solution:
    def maximalRectangle(self,matrix:List[List[str]])->int:
        """
        单调栈
        """
        rows ,cols = len(matrix),len(matrix[0])
        heights = [0]*cols ## 存储的是逐行累加的高度
        max_area = 0 # 结果

        ## 逐渐更新heights
        for row in matrix:
            for j in range(cols):
                if row[j]=='1':
                    heights[j]+=1
                else: ## 当前值为0,那就代表从上往下，到这里高度重置
                    heights[j]=0

            ## 每一次算完一行后，更新最大值
            max_area = max(max_area,self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self,heights):
        """
        利用单调栈，求最大矩形面积，参考求雨滴
        """
        stack = []
        max_area = 0
        heights.append(0) ## 哨兵,保证最后清空栈

        for i , h in enumerate(heights):
            while stack and heights[stack[-1]]>h: ## 说明以stack[-1]为高度的矩形结束了,求结果
                height = heights[stack.pop()]
                ## 左边界为当前的栈顶索引,右边界为i
                width = i if not stack else i-stack[-1]-1 ## 如果栈为空，说明可以延伸到最左边,压就是0-i就是宽度
                max_area = max(max_area , width*height)
            stack.append(i) ## 如果是单调增就直接添加
        
        ## 清空哨兵
        heights.pop()
        return max_area
        


