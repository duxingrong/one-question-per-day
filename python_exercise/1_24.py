"""
174.地下城游戏

恶魔们抓住了公主并将她关在了地下城dungeon的右下角。地下城里由mXn个房间组成的二维网格。我们英勇的骑士最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。

骑士的初始健康点数为一个正整数，如果他的健康点数在某一时刻降到0或以下，他会立即死亡。

有些房间有恶魔守卫，因此骑士在进入这些房间时会失去健康点数；其他房间要么是空的，要么包含增加骑士健康点数的魔法球

为了尽快解救公主，骑士决定每次只向右或向下移动一步。

返回取保骑士能够拯救到公主所需要的最低健康点数。

注意： 任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士键入的左上角房间以及公主被监禁的右下角房间。

"""

from typing import List
"""
唯一需要注意的就是这个逆向的动态规划
"""

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        # dp[i][j] 表示到达 (i, j) 时所需的最小健康点数
        dp = [[float('inf')] * n for _ in range(m)]

        # 初始化终点
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])

        # 初始化最后一列（除了终点）
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(1, dp[i + 1][n - 1] - dungeon[i][n - 1])

        # 初始化最后一行（除了终点）
        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = max(1, dp[m - 1][j + 1] - dungeon[m - 1][j])

        # 填充其他位置
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])

        return dp[0][0] # 这里一定会变成整数



"""
递归+缓存
"""
from functools import cache
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        # 递归函数，表示从(i,j)到达终点最低健康点数
        @cache
        def dfs(i:int,j:int)->int:
            # 最简单的逻辑
            if i==m-1 and j==n-1:
                return max(1,1-dungeon[i][j])

            # 一般的逻辑
            min_health = float('inf')

            # 向右边递归
            if j+1 < n :
                min_health = min(min_health,dfs(i,j+1))

            # 向下边递归
            if i+1 < m :
                min_health = min(min_health,dfs(i+1,j))

            # 计算当前位置的最低健康点数
            return max(1,min_health-dungeon[i][j]) 

        # 从起点(0,0)开始递归
        return dfs(0,0)

