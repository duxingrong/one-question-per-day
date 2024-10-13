"""
完全背包
就是每一个物品可以选很多次,来算背包j所能装下的最大价值


这里我们唯一和01背包有区别的就是遍历顺序从倒序变成了正序(为什么?)
dp[i][j]从0-i个物品中拿重量j的最大价值,我们现在时完全背包,那就要看第推公式的变化了

dp[i][j]=
1. 不选第i个物品.那就是dp[i-1][j]
2. 选第i个物品.那我现在要考虑到,选了之后,我还能再选这个物品吗?当然可以! 所以他时dp[i][j-weight[i]]+value[i](这里不需要把i-1,因为当前物品还能再选,所以选择的范围还是0-i!)
所以可以看到,当前的dp[j]只和他的上一层和他当前层的前面的值有关,所以滚动数组是顺序
而01背包是由于选过不能在选,所以选了当前物品后需要将范围-1.所以他是和上一层的左边值和正头上的值有关,那么滚动数组就要逆序
"""

from typing import List

class Solution():
    def test_CompletePack(self,weights:List[int],values:List[int],m:int,n:int)->int:#m个物品,容量为n
        # 初始化dp
        dp=[0]*(n+1) 
        
        for i in range(m):
            for j in range(weights[i],n+1):
                dp[j]=max(dp[j],dp[j-weights[i]]+values[i])
        print(dp)

        return dp[n]

weights=[1,3,4]
values=[15,20,30]
m=3 
n=4
solution=Solution()
print(solution.test_CompletePack(weights,values,m,n))

