class Solution:
    """
    887.鸡蛋掉落
    """
    def superEggDrop(self,k:int,n:int)->int:
        """
        动态规划+逆向
        dp[m][k]表示:有k个鸡蛋，最多m次操作数量，可以在多少楼层中判断出f
        鸡蛋落下后:
            1. 如果碎了,鸡蛋少了一个,次数又少了一次，这下最多能判断的楼层是dp[m-1][k-1]
            2. 如果没碎，鸡蛋没少，次数少了一次,这下最多能判断的楼层是dp[m-1][k]

            dp[m][k]=dp[m-1][k-1]  如果碎了，我们能查低层的部分
                    +dp[m-1][k]    如果没碎，我们能查高层那部分
                    +1             当前这一层
            这个“+号”确实是这个状态方程里最容易卡住的一点,你扔一次鸡蛋后，其实是把“楼层搜索区间”一分为二了
        """
        dp = [[0]*(k+1) for _ in range(n+1)]

        m=0 
        while dp[m][k]<n:
            m+=1
            for egg in range(1,k+1):
                dp[m][egg] = dp[m-1][egg-1]+dp[m-1][egg]+1
        return m


if __name__ == "__main__":
    solution = Solution()
    print(solution.superEggDrop(2,6))
