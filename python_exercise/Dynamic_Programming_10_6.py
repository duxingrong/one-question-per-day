"""

给定一个非负整数数组.a1,a2....an,和一个目标数S.现在有两个符号+-,对于数组中的任意一个整数.都可以从+或者-中选择一个符号添加在前面

返回可以使得最终数组和为目标和的所有添加符号的方法数


把前面加+号的为一堆P,然后前面为-号的为一堆N, 由P-N=S P+N=sum  -->P=(sum+S)//2
问题变成了找到所有和可以为(sum+S)//2的子数组

(每个元素只有两种状态.取或者不取,不能重复)
含义    : 容量为j的背包有dp[j]中方法装满
初始化  : dp[0]=1(表示凑满0容量的方法有1种,取空集)
递推公式: 
nums=[1,2,3,4,5].用dp[5]举例 
取1 时候  容量为4的背包有dp[4]种方法装满,那么你再取元素1(这是事实),那门dp[5]=dp[4]
取2 时候  容量为3的背包有dp[3]种方法装满,那么你再取元素2(这是事实),那门dp[5]=dp[3]
取3 时候  容量为2的背包有dp[2]种方法装满,那么你再取元素3(这是事实),那门dp[5]=dp[2]
取4 时候  容量为1的背包有dp[1]种方法装满,那么你再取元素4(这是事实),那门dp[5]=dp[1]
取5 时候  容量为0的背包有dp[0]种方法装满,那么你再取元素5(这是事实),那门dp[5]=dp[0]
所以dp[j]+=dp[j-num]
"""
from typing import List

class Solution():
    def findTargetSumWays(self,nums:List[int],S:int)->int:
        # 如果S绝对值>nums总和,说明全部取+or-都满足不了,没有方法
        if abs(S)>sum(nums):
            return 0

        # 判断有无target
        if (sum(nums)+S) % 2==1:
            return 0
        # 求出target
        target=(sum(nums)+S)//2
        # dp数组
        dp=[0]*(target+1)
        #初始化
        dp[0]=1

        for num in nums:
            for j in range(target,num-1,-1): #保证j-num>0
                dp[j]+=dp[j-num]
                # print(dp)
        return dp[target]


nums=[100]
S=-200
solution=Solution()
print(solution.findTargetSumWays(nums,S))

















