"""
给定一个整数数组nums，找到一个具有最大和的连续子数组(子数组最少包含一个元素),返回其最大和

连续 最大和


dp[i] 以nums[i-1]结尾的子数组的最大和为dp[i]

dp[i]=max(dp[i-1]+nums[i-1],nums[i-1]) #要么就加，要么就舍弃从新来
result=float('inf')
result=max(result,dp[i])
初始化:dp[0]=float('inf')
顺序
"""

from typing import List ,Optional

class Solution():
    def maxSubArray(self,nums:List[int])->Optional[int]:
        if len(nums)==0:
            return None
        #dp数组
        dp=[float('-inf')]*(len(nums)+1)
        result=float('-inf')

        for i in range(1,len(nums)+1):
            dp[i]=max(dp[i-1]+nums[i-1],nums[i-1])
            result=max(result,dp[i])

        return int(result)



nums=[-2,1,-3,4,-1,2,1,-5,4]
solution=Solution()
print(solution.maxSubArray(nums))


