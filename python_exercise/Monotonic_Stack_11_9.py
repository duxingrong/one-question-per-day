"""
给定n个非负数，用来表示柱状图中各个柱子的高度，每个柱子彼此相邻，且宽度为1

求在该柱状图中，能够勾勒出来的矩形的最大面积

这个题目和接雨水那个题目一样，接雨水是找到两边比他高的柱子，这个找到两边比他矮的柱子

我们这下就需要用到单调递减序列，但是还是有个问题，有的柱子会不会出栈，这就导致我们无法知道以他们为高的最大矩形，解决方法就是在数组的左右两边加上0,这样每个柱子都会拥有左右比他矮的柱子
"""

from typing import List

class Solution():
    def largestRectangleArea(self,nums:List[int])->int:
        #给nums左右两边加上0
        nums.insert(0,0) #(index,val)
        nums.append(0)

        #初始化
        result=0
        stack=[]

        for i in range(len(nums)):
            while len(stack)>0 and  nums[i]<nums[stack[-1]]:
                height=nums[stack[-1]]
                stack.pop()
                result=max(result,(i-stack[-1]-1)*height)
            stack.append(i)
        return result


nums=[2,1,5,6,2,3]
solution=Solution()
print(solution.largestRectangleArea(nums))
