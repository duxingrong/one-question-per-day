"""
53. 最大子数组和

给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组是数组中的一个连续部分

"""

"""
很标准的一个前缀和

当前前缀和 - 之前最小的前缀和。
"""

from typing import List 

class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        
        prefix_sum = 0 
        min_prefix_sum = 0 
        ans = nums[0]

        for num in nums:
            prefix_sum += num 
            
            #当前最大子数组和 = 当前前缀和 - 前面的最小前缀和
            ans = max(ans,prefix_sum-min_prefix_sum)

            # 更新最小前缀和
            min_prefix_sum = min(prefix_sum,min_prefix_sum)

        return ans 
    

"""
更经典的是动态规划

如果前面的和是负数，那继续接上它只会拖累当前数字，所以重新开始
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current_sum = 0 
        ans = nums[0]  # 不能初始化为0 

        for i in range(len(nums)):
            current_sum = max(current_sum+nums[i],nums[i])

            ans = max(ans, current_sum)

        return ans 