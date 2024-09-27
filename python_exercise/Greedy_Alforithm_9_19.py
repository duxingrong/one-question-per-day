"""
气球在二维空间上是数值向上飞的,我们可以知道沿着y轴气球的直径的开始位置和结束位置
一支弓箭可以沿着x轴从不同点完全垂直的射出,在坐标x处射出一支箭,若有一个气球的直径的开始和结束坐标为xstart,xend,且满足xstart<=x<=xend,则该气球,会被引爆.可以射出的弓箭的数量没有限制,共建一旦射出后,可以无限的前进,我们想找到使得所有气球全部被引爆所需的弓箭的最小数量
输入是points=二维数组,其中points[i]=[start[i],end[i]]
举例:
points=[[10,16],[2,8],[1,6],[7,12]]
ans = 2
"""

"""
怎么贪心才能贪最多?
这里的关键就是在于,我们可以想出来如何让判断当前的气球是否可以和上一个气球用一支箭头,但是怎么判断下一个气球也可以用同一支箭头呢?
这就是难点,我们利用更新右边界的方法完美实现需求
"""

from typing import List
class Solution():
    def findMinArrowShots(self,points:List[List[int]])->int:
        # 特殊情况
        if len(points)==0:
            return 0
        # 按左边界进行排序,方便看有没有交集
        points=sorted(points,key=lambda x:x[0])
        # 初始化
        ans=1

        for i in range(1,len(points)):
            if points[i][0]>points[i-1][1]:  # 如果当前气球的左边界都大于了上一个气球的右边界,那说明他两没交集,肯定需要加弓箭了
                ans+=1
            else: #这里才是精髓,我们更新右边界,来判断下一个气球能否被这支箭来覆盖!
                points[i][1]=min(points[i][1],points[i-1][1]) 
        return ans


points=[[10,16],[2,8],[1,6],[7,12]]
solution=Solution()
print(f"需要的箭数是:{solution.findMinArrowShots(points)}")




