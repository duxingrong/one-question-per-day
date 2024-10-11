"""
有一堆石头,每块石头的重量都是正整数
每一回合,从中选出任意两块石头,然后将它们一起粉碎,假设石头的重量分别为x和y,且x<=y.那么粉碎的可能结果如下:

1. x==y: 两块一起粉碎
2. x!=y: x粉碎, y=y-x
最后,最多只会剩下一块石头.返回此石头最小的可能重量.如果没有石头剩下.就返回0.
输入:[2,7,4,1,8,1]
输出:1

???这个怎么和01背包有关系???
这题目最难得就是要整体思想,尽量找到两堆尽可能一样的石头,让它们相碰.所以又回到了找到dp[j]所能装的最大重量(回归到01背包)

dp[j]: 重量为j的背包能装的最大重量dp[j]
dp[j]=max(dp[j],dp[j-nums[i]]+nums[i])
初始化: dp=[0]*(target+1)
遍历顺序:先遍历石头,然后遍历容量
"""
from typing import List

class Solution():
    def  lastStoneWeightII(self,nums:List[int])->int:
        # target
        target=sum(nums)//2
        # dp数组
        dp=[0]*(target+1)

        #遍历
        for num in nums:
            for j in range(target,num-1,-1): #保证dp[j-nums[i]]有意义
                dp[j]=max(dp[j],dp[j-num]+num)
        print(dp)

        return (sum(nums)-dp[target])-dp[target]  # 多的一堆石头去打少的石头

nums=[2,7,4,1,8,1]
solution=Solution()
print(solution.lastStoneWeightII(nums))

