"""

最长递增子序列的个数

给定一个未排序的整数数组,找到最长递增子序列的个数

[1,3,5,4,7] 输出: 2

[1,3,4,7] 和[1,3,5,7]

就可以确定为首先找到最长递增子序列的长度，然后寻找所有长度为最长的递增子序列个数

[2,2,2,2,2]
最长递增子序列长度为1,然后长度为1的递增子序列有5个

"""

"""
定义:
dp[i]:i 之前(包括i)最长递增子序列的长度为dp[i].
count[i]:以nums[i]为结尾的字符串,最长递增子序列的个数为count[i]

递推公式:
如果只是求最长递增子序列长度那就是dp[i]=max(dp[i],dp[j]+1)
但是这里还要求长度下的子序列个数,分类讨论:
如果是dp[j]+1>dp[i]:那就是说明发现了新的最长子序列,那么以i结尾的个数==以j结尾的个数
如果是dp[j]+1==dp[i]:那就是这两个长度一样，那么整体的以i结尾的个数就是count[i]+=count[j]

初始化:
dp[i] = 1 长度至少会是它自己
count[i]=1 个数至少也是它自己的长度,他自己算一个

遍历顺序:顺序
"""

from typing import List

class Solution():
    def findNumberOfLIS(self,nums:List[int])->int:
        n  = len(nums)
        #初始化
        dp = [1]*n 
        count = [1]*n 

        Maxcount=1 #记录最大长度
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp[j]+1>dp[i]: #说明最大长度更新
                        dp[i]=dp[j]+1 #长度更新
                        count[i]=count[j] #i结尾的最长子序列个数也更新
                    elif dp[j]+1 == dp[i]:
                        count[i]+=count[j] #i结尾的个数增加
                #更新最大长度
                if Maxcount<dp[i]:
                    Maxcount = dp[i]

        result = 0
        # 然后求出所有的个数
        for i in range(n):
            if dp[i]==Maxcount:
                result+=count[i]

        return result


        


