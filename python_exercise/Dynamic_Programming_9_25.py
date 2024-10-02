"""
斐波那契数,通常用F(n)表示,形成的数列称为斐波那契数列,该数列由0和1开始,后面的每一个数字都是前面两项数字的和,F(0)=0,F(1)=1,F(n)=F(n-1)+F(n-2)
输入n,输出F(n)
"""

"""
动态规划的五步
1. dp[i]的含义和下标定义: 表示第i个斐波那契数的值是dp[i]
2. 递推公式: dp[i]=dp[i-1]+dp[i-2]
3. dp数组如何初始化 : dp[0]=0, dp[1]=1
4. 遍历顺序 : 从左到右
5. 打印dp数组 
"""

class Solution():
    def fib(self,N:int)->int:
        # 特殊处理
        if N<2:
            return N
        # 初始化
        dp=[0]*( N+1 )
        dp[0]=0
        dp[1]=1
        for i in range(2,N+1):
            dp[i]=dp[i-1]+dp[i-2]
        # print(dp)
        return dp[N]

"""
我们不必要维护所有,只需要维护两个值就好
"""

class Solution():
    def fib(self,N:int)->int:
        # 特殊处理
        if N<2:
            return N
        dp=[0,1]
        for i in range(2,N+1):
            total=dp[0]+dp[1]
            dp[0]=dp[1]
            dp[1]=total
        return dp[1]

"""
递归(但是效率不高)
终止条件: 如果N<2: return N
单层逻辑: return 前两个值想加
"""

class Solution():
    def fib(self,N:int)->int:
        # 终止条件
        if N<2:
            return N
        return self.fib(N-1)+self.fib(N-2)











