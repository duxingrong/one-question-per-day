"""给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
示例：
输入s = 7, nums = [2,3,1,2,4,3]
输出2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
"""
#滑动窗口算法能够有效地在一次遍历中找到最短的满足条件的子数组，而不需要检查数组中的每一个子数组，从而大大提高了算法的效率。
from typing import List

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = len(nums)
        left = 0
        right = 0
        min_len = float('inf')
        cur_sum = 0 #当前的累加值
        
        while right < l:
            cur_sum += nums[right]
            
            while cur_sum >= s: # 当前累加值大于目标值
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            
            right += 1
        
        return min_len if min_len != float('inf') else 0

nums = [2, 3, 1, 2, 4, 3,7]
s = 7
solution = Solution()
print(solution.minSubArrayLen(s, nums))  # 注意这里参数顺序应为 (s, nums)