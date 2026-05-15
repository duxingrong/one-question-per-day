"""
最长连续序列

给定一个未排序的整数数组nums ,找出数字连续的最长序列(不要求序列元素在原数组中连续)的长度

请你设计并实现时间复杂度为O(n)的算法解决此问题

哈希set ，不排序，但只找每一段连续序列的开头，然后从开头往后数
"""

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # 排序
        num_set  = set(nums)

        ans = 0 

        for num in num_set:
            # 只有是开头，我们才往下数
            if num-1 not in num_set:
                cur_num = num 
                cur_len = 1 

                while cur_num+1 in num_set:
                    cur_len +=1 
                    cur_num +=1 


                ans = max(ans,cur_len)

        return ans 


