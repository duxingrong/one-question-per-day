"""
给定n个非负整数表示每个宽度为1的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水

例如 
height=[0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

接雨水的题目，双指针方法的话就是按照列来求，单调栈的方法的话就是按照行来求

我们单调栈，可以找到右边第一个比它高的柱子，然后栈里的第二个元素(栈顶的下一个)，就是他的左边第一个比他高的柱子(如果这里发现左边和它一样高，也没有关系，因为可以看作这个柱子的水它存不住)
面积= (min(left,right)-height)*宽度(右下标减去左下标-1)这里为什么减一，模拟一下就知道了
"""

from typing import List

class Solution():
    def trap(self,heights:List[int])->int:
        result=0 #初始化
        stack=[]

        for i in range(len(heights)):
            while len(stack)>0 and heights[i]>heights[stack[-1]]: #找到了右边的柱子
                height=heights[stack.pop()] #得道自己的高度
                if stack:
                    result+=(min(heights[stack[-1]],heights[i])-height)*(i-stack[-1]-1) #左右柱子的最小值-自己的高度 最后乘以宽度
            stack.append(i)
        return result

heights=[0,1,0,2,1,0,1,3,2,1,2,1]
solution=Solution()
print(solution.trap(heights))



"""

双指针
使用列来计算,那么宽度一定是1,我们把每一列的雨水的高度求出来就可以了

每一列雨水的高度，取决于它左边的柱子和右边的柱子的最小值
min(left,right)-height,所以我们只要知道每个位置它的左右最高柱子中的最小值，就可以求出来了

所以我们这里可以利用双指针，动态维护两个值，leftmax 和 rightmax
leftmax数组表示当前的这个值左边的最高柱子(包括自己的高度)
rightmax数组表示当前的这个值右边的最高柱子(包括自己的高度)
"""

from typing import List

class Solution():
    def trap(self,nums:List[int])->int:
        #首先记录每一个位置左边的最高柱子，这个包括他自己
        left=[0]*len(nums)
        right=[0]*len(nums)
        for i in range(len(nums)):
            if i ==0:
                left[i]=nums[i]
            else:
                left[i]=max([left[i-1],nums[i]])
        #每个位置右边的最高柱子
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                right[i]=nums[i]
            else:
                right[i]=max(right[i+1],nums[i])

        #遍历计算体积
        result=0
        for i in range(len(nums)):
            result+=min(left[i],right[i])-nums[i] #这里宽度为1,可以省略
        return result











