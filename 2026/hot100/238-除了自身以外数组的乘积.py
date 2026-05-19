"""
238. 除了自身以外数组的乘积

给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除了 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请 不要使用除法，且在 O(n) 时间复杂度内完成此题

"""

"""
除了自己以外的乘积 = 左边所有数的乘积 x 右边所有数的乘积
O(2n)也是O(n)
"""


from typing import List 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # 初始化答案
        answer = [1]*len(nums)

        # 先算左边
        left = 1 
        for i in range(len(nums)):
            answer[i] = left 
            left*=nums[i]

        # 右边
        right = 1 
        for i in range(len(nums)-1,-1,-1):
            answer[i] *= right
            right*= nums[i]

        
        return answer 

