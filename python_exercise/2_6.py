from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        计算在符合规则的情况下能够摘取的最多樱桃数。
        
        规则说明：
        1. 从起点 (0,0) 到终点 (n-1, n-1) 的路径只能向右或向下走；
        2. 到达终点后必须返回到起点 (0,0)，返回时只能向左或向上走；
        3. 当经过一个格子且该格子内有樱桃（值为 1）时，会摘取该樱桃，并使该格子变为 0；
        4. 格子中值为 -1 表示荆棘，不能经过这样的格子；
        5. 如果在起点到终点之间不存在一条有效路径，则返回 0。
        
        解题思路：
        将题目转换为：同时有两个人从 (0,0) 出发，一步步同步前进，均只能向右或向下走，
        最终同时到达 (n-1, n-1)。由于两人可能经过同一个格子，因此如果 (x1, y1) == (x2, y2)
        时，只能摘取一次该位置的樱桃。
        
        使用 dp[k][x1][x2] 表示经过 k 步后，第一个人位置为 (x1, k - x1)，第二个人位置为 (x2, k - x2) 时能够摘取的最多樱桃数。
        
        :param grid: 二维列表，表示樱桃地，每个元素的值为 0、1 或 -1。
        :return: 最大摘取樱桃数，如果无路径，则返回 0。
        """
        n = len(grid)
        # 初始化dp 大小为(2n-1)*n*n ，所有状态初始化为-1,这样才可以判断这个地方是否可以更新
        dp = [[[-1]*n for _  in range(n)] for _ in range(2*n-1)]

        dp[0][0][0] = grid[0][0] 

        # k表示走了多少步,范围是0,2n-2
        for k in range(1,2*n-1):
            # x的范围根据 0<=x<=n-1 和 0<=k-x1<=n-1来决定
            for x1 in range(max(0,k-n+1),min(n,k+1)):
                for x2 in range(max(0,k-n+1),min(n,k+1)):
                    y1 = k-x1
                    y2 = k-x2

                    #判断当前格子是否是荆棘
                    if y1>=n or y2>=n or grid[x1][y1]==-1 or grid[x2][y2]==-1:
                        continue

                    best = -1
                    for dx1,dy1 in ((-1,0),(0,-1)):
                        for dx2,dy2 in ((-1,0),(0,-1)):
                            px1,px2 = x1+dx1,x2+dx2
                            if 0<=px1<n and 0<=px2 <n:
                                prev = dp[k-1][px1][px2]
                                if prev>=0:
                                    best = max(best,prev)
                    # 如果前面没有一个位置可达，那么当前状态不成立
                    if best == -1:
                        continue

                    #如果两个位置重合，那么只算一次
                    if x1==x2 and y1==y2:
                        cherries = grid[x1][y1]
                    else:
                        cherries = grid[x1][y1]+grid[x2][y2]


                    dp[k][x1][x2] = cherries + best

        return max(dp[2*n-2][n-1][n-1] ,0)



