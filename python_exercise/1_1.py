"""
切蛋糕的最小总开销||

有一个m*n大小的矩形蛋糕,需要切成1*1的小块

给你整数m,n和两个数组:

horizontalCut的大小为m-1,其中horizontalCut[i]表示沿着水平线i切蛋糕的开销

verticalCut的大小为n-1,其中verticalCut[j]表示沿着垂直线j切蛋糕的开销

一次操作中,你可以选择任意不是1*1大小的矩形蛋糕并执行以下操作之一:
1.沿着水平线i切开蛋糕,开销为horizontalCut[i].
2.沿着垂直线j切开蛋糕,开销为verticalCut[j].
每次操作后的开销都为最开始对应切割线的开销,并且不会改变
请你返回将蛋糕全部切成1*1的蛋糕快的最小总开销

m=3, n=2,horizontalCut=[1,3],verticalCut = [5]
输出13

可以用贪心的思想来解决,首先我们要知道，每一次动刀后,蛋糕的块数都是增加的，所以权重大的一定要提前切割

每一次的开销 : 如果是垂直 = 你当前这刀的权重*水平蛋糕块的个数

               如果是水平 = 你当前这刀的权重*垂直蛋糕块的个数
"""

from typing import List

class Solution():
    def minimumCost(self,m:int,n:int,horizontalCut:List[int],verticalCut:List[int])->int:

        # 将数组按照从大到小的顺序
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        # 变量
        i,j = 0,0  #用来记录从数组中拿了几次
        h_blocks,v_blocks = 1,1 #垂直蛋糕和水平蛋糕的块数
        total_cost = 0 #记录结果

        # 主程式
        while i<len(horizontalCut) and j<len(verticalCut):
            # 比较当前谁的权重更大
            if horizontalCut[i]>verticalCut[j]:
                total_cost+= horizontalCut[i]*v_blocks
                i+=1
                h_blocks+=1
            else:
                total_cost += verticalCut[j]*h_blocks
                j+=1
                v_blocks+=1

        ## 当还有还有剩余的没切,下面两个循环只会有一个进行
        while i<len(horizontalCut):
            total_cost+= horizontalCut[i]*v_blocks
            i+=1

        while j<len(verticalCut):
            total_cost+= verticalCut[j]*h_blocks
            j+=1

        return total_cost

if __name__=="__main__":
    horizontalCut = [1,4,5,7,8]
    verticalCut  = [3,4,5,6,7]
    m = 6
    n = 6
    solution = Solution()
    print(solution.minimumCost(m,n,horizontalCut,verticalCut))
            

