"""
数组的每个下标作为一个阶梯,第i个阶梯对应着一个非负数的体力花费值cost[i],每当你爬上一个阶梯你都要花费对应的体力值,一旦支付了相应的体力值,你就可以向上爬一个阶梯或者是两个阶梯
找出到达楼顶部的最低花费,在开始时,你可以选择从下标为0或者1的元素作为初始阶梯

输入: cost=[10,15,20]
输出: 15
从cost[1]开始走然后选择走两步,花费15
"""

"""
动态规划5步骤
1. dp[i]的含义和下标定义:  到这第i阶的最小花费为dp[i]
2. 递推公式:  dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2]),应该可以理解,你就是如果是从i-1挑上来,那就时加上i-1的花费...
3. dp数组如何初始化 : i由i-1和i-2推出,所以需要初始化dp[0]和dp[1], 由由题目,我们站在0和1的位置是没有花费的,是往上面挑时才要花费 dp[0]=dp[1]=0
4. 遍历顺序 : 从左到右
5. 打印dp数组 
"""

from typing import List

class Solution():
    def minCostClimbingStairs(self,cost:List[int])->int:
        # dp数组以及初始化
        dp=[0]*(len(cost)+1)
        dp[0]=dp[1]=0

        for i in range(2,len(cost)+1):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])

        return dp[len(cost)]

"""
同样可以只维护3个数
"""

from typing import List

class Solution():
    def minCostClimbingStairs(self,cost:List[int])->int:

        dp=[0,0]
        for i in range(2,len(cost)+1):
            val=dp[1]
            dp[1]=min(dp[0]+cost[i-2],dp[1]+cost[i-1])
            dp[0]=val
        return dp[1]





"""
这个是最开始自己想的,还是有局限性,对于cost=[0,2,2,1]就失败了
"""
from typing import List

class Solution():
    def minCostClimbingStairs(self,cost:List[int])->int:
        if len(cost)==1:
            return cost[0]
        self.result=0
        i=len(cost)
        while i>=2:
            if cost[i-1]>=cost[i-2]:
                self.result+=cost[i-2]
                i=i-2
            elif cost[i-1]<cost[i-2]:
                self.result+=cost[i-1]
                i=i-1
        return self.result



cost=[1,100,1,1,1,100,1,1,100,1]
solution=Solution()
print(solution.minCostClimbingStairs(cost))









