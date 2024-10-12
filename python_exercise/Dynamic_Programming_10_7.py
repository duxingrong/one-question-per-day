"""
给你一个二进制字符串数组strs和两个整数m和n
请找出并且返回strs的最大子集的大小.该子集中最多有m个0和n个1

输入: strs=["10","0001","111001","1","0"],m=5,n=3
输出: 4  最大子集是["10","0001","1","0"]

这又和01背包有什么关系阿?
每个元素只有取或者不取
这个题目关键在于理解背包成了两个纬度.一个是装满0,一个是装满1.

所以dp[i][j]: 装满i个0和j个1的最大子集数量为dp[i][j]
dp[i][j]=max(dp[i][j](不取当前的元素),dp[i-zeronum][j-onenum]+1(取当前的元素))
初始化: 由于是取最大值,所以初始化为0 ,dp[0][0]=0
遍历顺序,先遍历物品,然后遍历背包(倒序)
打印调试
"""
from typing import List

class Solution():
    def findMaxForm(self,strs:List[str],m:int,n:int)->int:
        #dp数组及初始化
        dp=[[0]*(n+1) for _ in range(m+1)]

        # 遍历物品和背包
        for str in strs:
            zeronum=str.count("0")
            onenum=len(str)-zeronum
            for i in range(m,zeronum-1,-1):
                for j in range(n,onenum-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-zeronum][j-onenum]+1) #不取和取比较,取子集数更多的
        print(dp)

        return dp[m][n]


strs=["10","0001","111001","1","0"]
m=5
n=3
solution=Solution()
print(solution.findMaxForm(strs,m,n))

"""
总结所有的01背包题目
原题: 是求装满容量的最大价值为?
分割等和子集:是求能否将容量j用物品装满
最后一块石头:是看将容量石头尽可能的装满,能装多少是多少
目标和:是看能装满背包的所有方法
1和0,是看将二维背包装满的最大子集数量
"""        

