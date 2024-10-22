"""
给定一个未经排序的整数数组，找到最长且连续严格递增的子序列,并返回该序列的长度

dp[i] :以nums[i]结尾的最长连续子序列的长度为dp[i]
if nums[i]>nums[i-1]:
    dp[i]=dp[i-1]+1
"""


from typing import List

class Solution():
    def findLengthOfLCIS(self,nums:List[int])->int:
        if len(nums)<=1:
            return len(nums)

        dp=[1]*(len(nums))
        result=1

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                dp[i]=dp[i-1]+1
            result=max(result,dp[i])
        print(dp)
        return result



nums=[1,3,5,4,7]

solution=Solution()
print(solution.findLengthOfLCIS(nums))


