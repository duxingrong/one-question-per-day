"""
移动零

给定一个数组nums,编写一个函数将所有0移动到数组的末尾，同时保持非零元素的相对顺序

请注意，必须在不复制数组的情况下原地对数组进行操作


用指针记录下一个非零元素应该放的位置，然后后面全部置零

"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        slow = 0 # 指针

        for i in range(len(nums)):
            if nums[i] != 0 :
                nums[slow] = nums[i]
                slow +=1 
            
        # 全部置零
        for i in range(slow,len(nums)):
            nums[i] = 0

