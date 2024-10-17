"""
你是一个专业的小偷,计划偷窃沿街的房屋,每间房间内都有一定的现金.这个地方所有的房屋都围绕一圈,这意味着最后一间房间和第一个房间是紧紧挨着的,同时.相邻的房屋装有相互连通的防盗系统.如果两间相邻的房屋在同一晚上被小偷闯入,系统就会自动报警

唯一的区别就是首尾连接了怎么在代码中体现呢?
分成两种情况就好了
1. 第一个房间偷, 那houses就从0到len(houses)-2
2. 第一个房间不偷,那houses就从1到len(houses)-1

"""
from typing import List

class Solution():
    def rob2(self,houses:List[int])->int:
        if len(houses)<=2:
            return max(houses)
        #两种情况
        return max(self.function(houses[:len(houses)-1]),self.function(houses[1:len(houses)])) #从0到倒数第二个,和1到最后一个
    
    def function(self,houses:List[int])->int:
        dp=[0]*len(houses)
        #初始化
        dp[0]=houses[0]
        dp[1]=max(houses[0],houses[1])

        for i in range(2,len(houses)):
            dp[i]=max(dp[i-1],dp[i-2]+houses[i])

        return dp[len(houses)-1]

houses=[1,2,3,1]
solution=Solution()
print(solution.rob2(houses))
        
