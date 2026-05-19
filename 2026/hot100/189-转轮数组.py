"""
189. 轮转数组

给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数


输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]

你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗

"""

"""
右轮转- 三次反转 全反转 前k反转 剩余反转
"""

from typing import List 

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # K取余
        k = k % len(nums)
        n = len(nums)

        def reverse(left:int,right:int)->None:
            while left < right:
                nums[left],nums[right] = nums[right], nums[left]
                left +=1 
                right -=1 
        
        # 全反转
        reverse(0,n-1)

        # 前k反转
        reverse(0,k-1)

        # 其余反转
        reverse(k,n-1)

        

        