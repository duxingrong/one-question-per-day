"""
560. 和为 K 的子数组

给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列

"""

"""

区间和等于前缀和相减
"""

from collections import defaultdict
from typing import List 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # 计算前缀和
        prefix = [0]*(len(nums)+1)

        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]

        ans = 0 
        hashmap = defaultdict(int)

        # 区间和等于k ，采用哈希
        for j in range(len(prefix)):

            # 判断
            if hashmap and prefix[j]-k in hashmap:
                ans += hashmap[prefix[j]-k]
            
            # 加入
            hashmap[prefix[j]]+=1
            
        return ans 



            
