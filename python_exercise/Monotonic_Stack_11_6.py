"""
给你两个没有重复元素的数组nums1和nums2,其中nums1是nums2的子集

请你找出nums1中每个元素在nums2中的下一个比其大的值


这里关键词，下一个比其大的值，标准的单调栈，并且是递增


这里就是递增单调栈套了一个壳子
需要在收获结果的时候看是不是nums1中的元素
"""
from typing import List

class Solution():
    def nextGreaterElement(self,nums1:List[int],nums2:List[int])->List[int]:
        #初始化
        stack=[]
        result=[-1]*len(nums1)

        for i in range(len(nums2)):
            while len(stack)>0 and nums2[i]>nums2[stack[-1]]:
                if nums2[stack[-1]] in nums1:
                    result[nums1.index(nums2[stack[-1]])]=nums2[i]
                stack.pop()
            stack.append(i)
        return result


        

