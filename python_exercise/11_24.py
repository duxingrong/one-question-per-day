"""
有多少个小于当前数字的数字
给你一个数组nums,对于其中每个元素nums[i],请你统计数组中比它小的所有数字的树目
换而言之，对于每个nums[i]你必须计算出有效的j的数量，其中j满足j!= i 且 nums[j]<nums[i]
以数组的形式返回答案
"""


from typing import List
from collections import defaultdict


class Solution():
    #暴力解法
    def function(self,nums:List[int])->List[int]:
        result = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j :
                    continue
                if nums[j]<nums[i]:
                    result[i]+=1
        return result

    """
    核心就是要知道每个数字在数组中比他小的数字的个数
    1. 排序
    2. 哈希(这里有技巧，倒序来解决相同的数字)
    """

    def smallerNumbersThanCurrent(self,nums:List[int])->List[int]:
        #排序
        res = nums.copy() #复制
        res = sorted(res)
        hash = defaultdict(int)
        #倒序来填充哈希
        for i in range(len(res)-1,-1,-1):
            hash[res[i]] = i

        #然后赋值
        for i in range(len(nums)):
            res[i]= hash[nums[i]]

        return res


if __name__ == "__main__":
    solution = Solution()
    nums=[8,1,2,2,3]
    result = solution.smallerNumbersThanCurrent(nums)
    print(result)



