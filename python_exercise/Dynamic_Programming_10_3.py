"""
01背包问题,使用一纬的数组解决
有n件物品和一个最多能背重量为w的背包,第i件物品的重量时weight[i],得到的价值是value[i].每件物品只能用一次,求解将哪些物品装入背包里物品价值总和最大

|dp[i][j] | 0  |  1  |   2  |   3  |   4 | 
| 0       | 0  |  15 |  15  |  15  |  15 |
| 1       | 0  |  15 |  15  |  20  |  35 |
| 2       | 0  |  15 |  15  |  20  |  35 | 
滚动数组其实就上将这上面的这个列表压缩成一行.就是将第一行保存到第二行的赋值中.因为我们的dp[i][j]= max(dp[i-1][j](不加i),dp[i-1][j-weight[i]+value[i](加i)]) 看得出来当前行的赋值只和上一行有关

1. dp[j]的含义和下标定义:   容量为j的背包最多的总价值
2. 递推公式: dp[j]=max(dp[j],dp[j-weight[i]]+value[i])
3. dp数组如何初始化 : dp[0]=0就好.后面的都可以推出来
4. 遍历顺序 :  必须先遍历物品,然后逆序遍历背包(因为我们只有一行数组,数据是要根据前面的dp[]来推出当前这一行后面的dp)
5. 打印dp数组 

"""

from typing import List

class Solution():
    def knapsack_01(self,n:int,w:int,weight:List[int],value:List[int])->int:
        # dp数组
        dp=[0]*(w+1)
        # 初始化
        dp[0]=0
        # 遍历赋值
        for i in range(n): #物品
            for j in range(w,-1,-1): #逆序背包
                if j>=weight[i]:
                    dp[j]=max(dp[j],dp[j-weight[i]]+value[i])
                else:
                    dp[j]=dp[j]
        return dp[w]


# 示例数据
n = 4  # 物品数量
w = 8  # 背包最大承重
weight = [1, 3, 4, 5]  # 物品重量
value = [1, 4, 5, 7]  # 物品价值
# 调用函数
solution = Solution()
max_value=solution.knapsack_01(n, w, weight, value)
print("背包能够获得的最大价值为:", max_value)

