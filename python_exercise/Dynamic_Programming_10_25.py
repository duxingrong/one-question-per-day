"""
给你一个整数数组nums,找到其中最长严格递增子序列的长度
"""

"""
dp[i]  以nums[i]结尾的最长递增子序列的最大个数为dp[i]
for i in range(1,len(nums)):
for j in range(0,i):
if nums[i]>nums[j]:
dp[i]=max(dp[i],dp[j]+1)  这里的意思就是,我这个位置的最长递增子数组要看接在前面所有比他小数字的后面从中选出来的最大个数
初始化
dp[0]=1
从前往后
"""

from typing import List

class Solution():
    def lengthOfLIS(self,nums:List[int])->int:
        if len(nums)==0:
            return 0
        #dp树组
        dp=[1]*(len(nums)) #为什么初始化为1,因为每个位置他自己肯定算递增,至少是1
        result=1

        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
            result= max(result,dp[i])
        return result

nums=[10,9,2,5,3,7,101,18]

solution=Solution()
print(solution.lengthOfLIS(nums))
