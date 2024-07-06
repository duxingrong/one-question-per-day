"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9

所以返回 [0, 1]
"""
from typing import List  
class Solution:  
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        records = dict()  # 初始化一个空字典，用于存储已经遍历过的数字及其索引

        for index, value in enumerate(nums):  # 遍历列表nums
            if target - value in records:  # 检查字典中，是否存在一个数与当前值相加等于target
                return [records[target - value], index]  # 如果存在，返回这个数的索引和当前值的索引
            records[value] = index  # 如果不存在，将当前值和它的索引存入records字典中
        return [] 

nums = [2, 7, 11, 15]  
n = 9  
solution = Solution()  
result = solution.twoSum(nums, n)  
print(result) 
            
        

