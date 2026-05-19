"""
41. 缺失的第一个正数

给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

"""

"""
关键在于思想： 把每个正整数放到它应该在的位置上，然后再遍历，发现不对的地方就是缺少的最小正整数
"""

from typing import List 

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)
        
        # 把每个正整数放在应有的位置
        for i in range(len(nums)):

            while 1 <= nums[i] < n and nums[nums[i]-1] != nums[i]: # 首先这个值是我们需要摆放的正整数，且防御重复
                correct_index = nums[i]-1 
                nums[i],nums[correct_index] = nums[correct_index],nums[i]


        # 然后遍历，第一个不是的就是缺失的最小正整数
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1 
        

        # 如果1到n都在正确位置，那就返回n+1 

        return n+1 