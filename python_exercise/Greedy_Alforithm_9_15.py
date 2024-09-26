"""
在一条环路上有N个加油站,其中第i个加油站有汽油gas[i]升
你有一辆油箱容量无限的汽车,从第i个加油站开往第i+1个加油站需要消耗汽油cost[i]升,你从其中的一个加油站出发,开始时候油箱为空
如果你可以环绕路行使一周,则返回出发时加油站的编号,否则返回-1
"""

"""
例如
gas  = [2,5,2,3,5]
cost = [1,2,8,2,4]
我们要把注意力放在每个站剩余的油上面(就是我们从这个站点去)
剩余油=[1,3,-6,1,1] 
首先考虑大局观的话,如果总的gas<cost的话,那不管怎样都是跑不完一圈的
然后我们现在每次将每一站的剩余油累加起来,如果发现剩余油<0了,说明在这之前的所有站都是做不了出发站的(因为我们是累加阿,你前面的站台每一次都会增加你的剩余油,然而你却还是不够到下一个站台),所以出发站台只能是在i+1后面,那出发站就重置为i+1,并且重置剩余油.然后继续遵守这个逻辑
"""
from typing import List

class Solution():
    def function(self,gas:List[int],cost:List[int])->int:
        total_sum=sum(gas)-sum(cost)
        # 总量小于那就直接返回
        if total_sum<0:
            return -1
        # 初始化
        current_sum=0
        start_index=0
        for i in range(len(gas)):  # 长度对了就行
            current_sum+=gas[i]-cost[i]
            if current_sum<0:
                start_index=i+1
                current_sum=0
        return start_index

gas  = [2,5,2,3,5]
cost = [1,2,8,2,4]
# gas  = [2,3,4]
# cost = [3,4,3]
#

solution=Solution()
start_index=0
if solution.function(gas,cost)==-1 :
    print(f"没办法环绕一圈")
else:
    print(f"出发站是{solution.function(gas,cost)}")

