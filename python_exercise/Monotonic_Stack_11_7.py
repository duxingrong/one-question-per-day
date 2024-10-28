"""
给定一个循环数组(最后一个元素的下一个元素是数组的第一个元素),输出每一个元素的下一个最大元素。数字x的下一个更大的元素是按照数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个最大的数 ，如果不存在，就输出-1

输入: [1,2,1]
输出: [2,-1,2]



循环遍历的话可以使用取摸的操作
i=(i+1)%len(nums)
这样最后一个元素的下一个i会成为0,循环了

循环的话，无非就是遍历两遍就好

"""

from typing import List

class Solution():
    def nextGreaterElements(self,nums:List[int])->List[int]:
        result=[-1]*len(nums)
        stack=[]

        for i in range(len(nums)*2):
            while len(stack)>0 and nums[i%len(nums)]>nums[stack[-1]]:  #满足条件
                result[stack[-1]]=nums[i%len(nums)]
                stack.pop()
            stack.append(i%len(nums))
        return result


            



