"""
多重背包的理论基础:
有N中物品和一个容量为V的背包,第i种物品最多有Mi件可用,每件耗费的空间是ci,价值是wi,求解将哪些物品装入背包可使得这些物品的耗费的空间总和不超过背包容量.且价值总和最大.
其分析本质就是和01背包的区别就是它有物品是一样的罢了

dp[j]装满容量j的最大的价值是dp[j]
是01所以先遍历物品,后遍历背包,逆序,这里由于是有物品有多个,所以再加一个for 循环来遍历个数就好了
比如遍历到第i物品
然后背包容量为j
因为i有多个,所以考虑放几个
for k in range(1,M[i]+1):
if k*weight[i]>j:
    break(剪枝)
当前如果取: 那就是dp[j]=dp[j-weight[i]*k]+value[i]*k 当k等于1时候,和01背包的公式一模一样
如果不取:   那就是dp[j]=dp[j](滚动数组)

"""
from typing import List

class Solution():
    def fuction(self,N:int,V:int,M:List[int],C:List[int],W:List[int])->int:
        #dp数组以及初始化
        dp=[0]*(V+1)

        for i in range(N):
            for j in range(V,C[i]-1,-1):
                for k in range(1,M[i]+1):
                    if k*C[i]>j:
                        break
                    dp[j]=max(dp[j],dp[j-C[i]*k]+W[i]*k)
        print(dp)
        return dp[V]

"""
二进制拆分来节省时间
他的核心就是利用如果一个物品1有13个,那么我们不需要遍历13次,而是利用二进制拆分.把物品拆分成1,2,4,..直到剩余小于二进制(分别记作物品1.1,1.2...)
这样做的目的就是可以减少遍历次数,为什么?因为取3个物品1等价于取物品1.1和物品1.2.取5等价于取1.2,1.3
所以当物品我们利用二进制转换成不同重量的物品时,我们遍历的次数减少,但效果和逐个遍历物品的数量是一样的
我们k 怎么取1,2,4....呢?
利用 k=1  while  k < amount:  for j in range(V,cost*k-1,-1): dp[j]=max(dp[j],dp[j-cost*k]+value*k)  amount-=k k*=2
直到剩余的 if amount>0: for j in range(V,amount*cost-1,-1): dp[j]=max(dp[j],dp[j-cost*amount]+value*amount)  
"""


class Solution1():
    def fuction(self,N:int,V:int,M:List[int],C:List[int],W:List[int])->int:
        #初始化dp
        dp=[0]*(V+1)
        #遍历物品
        for i in range(N):
            amount=M[i]
            cost=C[i]
            value=W[i]

            #二进制拆分
            k=1
            while k<amount:
                for j in range(V,cost*k-1,-1):
                    dp[j]=max(dp[j],dp[j-cost*k]+value*k)
                amount-=k
                k*=2
            if amount>0:
                for j in range(V,amount*cost-1,-1):
                    dp[j]=max(dp[j],dp[j-cost*amount]+value*amount)

        return dp[V]


