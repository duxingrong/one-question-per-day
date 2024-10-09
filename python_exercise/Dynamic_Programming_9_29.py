"""
一个机器人位于mxn的网络的左上角,机器人每次只能向下或者向右移动一步,机器人试图达到网络的右下角,问总共有多少条不同的路径
现在考虑网络中有障碍物,那么从左上角到右下角将会有多少条不同的路径
网络中的障碍物和空位置分别用1和0表示
"""

"""
动态规划5步骤
1. dp[m][n]的含义和下标定义:  m行n列位置的路径有dp[m][n]种
2. 递推公式:  dp[m][n]=dp[m-1][n]+dp[m][n-1]  如果这个位置有石头,那就这个位置=0
3. dp数组如何初始化 :  如果第一行和第一列有石头,那就之前的为1,后面的全部为0
4. 遍历顺序 :  从左上角到右下角
5. 打印dp数组 
"""
from typing import List

class Solution():
    def uniquePathsWithObstacles(self,obstacleGrid:List[List[int]])->int:
        # 怎么初始化dp数组?
        dp=[[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]

        

        # 初始化第一行和第一列
        for i in range(len(dp[0])):
            if obstacleGrid[0][i]==1:# 一旦有石头,后面的路径都是0
                break
            dp[0][i]=1

        for i in range(len(dp)):
            if obstacleGrid[i][0]==1:# 一旦有石头,下面的路径都是0
                break
            dp[i][0]=1

        # 判断起点是否有石头
        if obstacleGrid[0][0]==1:
            return 0

        # 开始递推
        for row in range(1,len(dp)):
            for col in range(1,len(dp[0])):
                if obstacleGrid[row][col]==1:
                    dp[row][col]=0
                else:
                    dp[row][col]=dp[row-1][col]+dp[row][col-1]
        print(dp)
        return dp[len(dp)-1][len(dp[0])-1]


obstacleGrid=[[0,0,0],[0,1,0],[0,0,0]]
solution=Solution()
print(solution.uniquePathsWithObstacles(obstacleGrid))
















