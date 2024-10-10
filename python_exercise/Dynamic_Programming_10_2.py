"""
01背包,有n件物品和一个最多能背重量为w的背包,第i件物品的重量时weight[i],得到的价值是value[i].每件物品只能用一次,求解将哪些物品装入背包里物品价值总和最大
"""

"""
动态规划5步骤(二维dp数组)
1. dp[i][j]的含义和下标定义:   在0-i个物品中任取容量为j的最大价值为dp[i][j]
2. 递推公式: 因为每个物品只有两种状态,取或者不取  
- 如果取第i个物品:(说明前0-i-1个物品只取容量为j-weight[i]) =dp[i-1][j-weight[i]]+value[i], 
- 不取第i个物品:(说明i-1个物品占了容量j)= dp[i-1][j]
举例 背包重量为4, 物品0:重1,价值15  物品1:重3,价值20  物品3:重4,价值30  
|dp[i][j] | 0  |  1  |   2  |   3  |   4 | 
| 0       | 0  |  15 |  15  |  15  |  15 |
| 1       | 0  |  15 |  15  |  20  |  35 |
| 2       | 0  |  15 |  15  |  20  |  35 | 
得出答案未35
3. dp数组如何初始化 : 从表格可以看出: 第一列dp[i][0]=0 (每个容量肯定价值全为0) 第一行dp[0][weight[0]-1]为0 ,后面的全部=value[0]
4. 遍历顺序 :  这里我们其实先遍历背包还是先遍历物品,都可以,因为dp[i-1][j-weight[i]]+value[i]和dp[i-1][j] 都在前面,不影响取值
5. 打印dp数组 
"""
from typing import List

class Solution():
    def knapsack_01(self,n:int,w:int,weight:List[int],value:List[int])->int:
        # dp 数组
        dp=[[0]*(w+1) for _ in range(n)]
        print(dp)

        # 初始化第一行(第一列由于本来赋值是0,所以不用重复初始化)
        for i in range(w+1):
            if i < weight[0]:
                dp[0][i]=0
            else:
                dp[0][i]=value[0]

        # 开始遍历赋值(先后遍历无所谓,都可以)
        for i in range(n):
            for j in range(w+1):
                if j>=weight[i]:
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i])
                else:
                    dp[i][j]=dp[i-1][j]
        
        return dp[n-1][w]


# 示例数据
n = 4  # 物品数量
w = 7  # 背包最大承重
weight = [1, 3, 4, 5]  # 物品重量
value = [1, 4, 5, 7]  # 物品价值
# 调用函数
solution = Solution()
max_value=solution.knapsack_01(n, w, weight, value)
print("背包能够获得的最大价值为:", max_value)




