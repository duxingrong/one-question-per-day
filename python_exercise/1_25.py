"""

2209.用地毯覆盖后的最少白色砖块

给你一个下标从0开始的二进制字符串floor,他表示地板上砖块的颜色

floor[i]='0'表示地板上第i块砖块的颜色是黑色。
floor[i]='1'表示地板上第i块砖块的颜色是白色。

同时给你numCarpets和carpetien。你有numCarpets条黑色的地毯，每一条黑色的地毯长度都为carpetien块砖块。请你使用这些地毯去覆盖砖块，使得未被覆盖的剩余白色砖块的数目最小。地毯相互之间可以覆盖。

请你返回没被覆盖的白色砖块的最少数目。

"""

class Solution:
    def minimumWhiteTiles(self,floor:str,numCarpets:int,carpetLen:int)->int:

        n = len(floor)

        # dp[i][j],表示前面i块砖用j条地毯后剩余的白色砖块的最少数量
        # dp[0][0] 当然为0
        dp = [[0]*(numCarpets+1) for _ in range(n+1)]

        # 初始化dp[i][0]
        for i in range(1,n+1):
            dp[i][0] = dp[i-1][0]+(1 if floor[i-1]=="1" else 0)

        # 填表

        for i in range(1,n+1):
            for j in range(1,numCarpets+1):
                # 第一种:在第i块砖不使用地毯
                dp[i][j]=dp[i-1][j]+(1 if floor[i-1]=='1' else 0)

                # 第二种，使用一条地毯来覆盖[i-carpetLen+1,i]的区间,如果够长直接覆盖所有
                if i>=carpetLen:
                    dp[i][j]=min(dp[i][j],dp[i-carpetLen][j-1])
                else:
                    dp[i][j]=min(0,dp[i][j])

        return dp[n][numCarpets]


"""
递归+记忆
"""

from functools import lru_cache

class Solution:
    def minimumWhiteTiles(self,floor:str,numCarpets:int,carpetLen:int)->int:
        n = len(floor)
        # 与处理:计算前缀和方便快速统计区间内白色砖快的数量
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+(1 if floor[i]=='1'else 0)

        # dp函数,从第i块砖开始(0为第一)，使用k块地毯后的最小白色数量
        @lru_cache(maxsize=None)
        def dp(i:int , k:int)->int:
            # 最简单的递归
            # 如果i>=n,超出长度，返回0
            if i>=n:
                return 0
            ## 如果k==0,那么可以直接求出
            if k==0:
                return prefix[n]-prefix[i]

            # 一般的推理逻辑
            ## 不放地毯，那就是保留当前的颜色，从下一块继续
            option1 = (1 if floor[i]=='1'else 0)+dp(i+1,k)

            ## 放地毯,那么就是只需要计算从i+carpetLen开始的最小白色数量
            option2 = dp(i+carpetLen,k-1)

            return min(option1,option2)

        return dp(0,numCarpets)



