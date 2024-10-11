"""
给定一个只包含正整数的非空数组,是否可以将这个数组分割成两个子集,使得两个子集的元素和相等

这个题目都可以抽象成01背包?
dp[j] 表示容量为j的背包所能装下的最大价值
这题目我们将重量==价值.就是判断dp[target]==target?  也就是容量为一半的背包一定要装进对应的这么多的价值,才说明有物品的价值(元素和)等于背包容量(sum(nums)//2)
通俗的话来说的话就是我的目标(价值和)target=sum(nums)//2,我要看我的背包所装物品的价值和能否等于target
例如: nums=[3,5,11,7]   target=13  nums=[1,5,11,7] target=12
一共就两种状态 
- dp[j]<target : dp[13]=12 ,这就说明不能分割成两个元素和想等的子数组
- dp[j]==target: dp[12]=12 ,想等了就说明有物品的价值等于目标价值 也就可以分成两个

既然是01背包问题了那就直接写了
"""
from typing import List

class Solution():

    def canPartition(self,nums:List[int])->bool:
        # 和为奇数直接False
        if sum(nums)%2==1:
            return False
        # 目标价值
        target=sum(nums)//2
        # dp数组,初始化为0(后面是取最大值,所以初始化小的)
        dp=[0]*(target+1)

        for i in range(len(nums)):
            for j in range(target,nums[i]-1,-1): # 这里要保证j-nums[i]>=0,不然会越界
                dp[j]=max(dp[j],dp[j-nums[i]]+nums[i])
        print(dp)

        if dp[target]==target:
            return True

        return False
        
nums=[1,5,11,5]
solution=Solution()
print(solution.canPartition(nums))
