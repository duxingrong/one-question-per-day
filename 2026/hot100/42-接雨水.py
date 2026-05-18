"""
42. 接雨水

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水

"""

"""
这里的关键就是在于弹出来的元素，要理解它是被夹住的，所以才能形成雨水
"""


from typing import List 

class Solution:
    def trap(self, height: List[int]) -> int:
        
        ans = 0 # 答案

        heap = [] # 单调递减栈

        for i in range(len(height)):

            
            while heap and  height[i] >= height[heap[-1]]:
                # 弹出的这个是坑底
                bottom = heap.pop() 
                # 如果弹出坑底后，左边没有墙了，就接不了水
                if not heap : break 
                # 弹出之后的栈顶才是left 
                left = heap[-1]
                # 右墙是当前的柱子
                right = i 

                # 宽度
                width = right-left-1 

                # 高度: 左右墙较矮的那个 - 坑底高度
                bounded_height = min(height[left],height[right]) - height[bottom]

                ans += width * bounded_height

            heap.append(i)

            

        return ans 

