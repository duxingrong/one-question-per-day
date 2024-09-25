"""
如果连续数字之间的差严格地在正数和负数之间交替,则数字序列称为摆动序列,少于两个元素的序列也是摆动序列
给定一个整数序列,返回作为摆动序列的最长子序列的长度,通过从原始序列中删除一些(也可以不删除)元素来获得子序列,剩下的元素保持其原始顺序
"""


"""
这里真是贪心算法的本质体现:我们不关心全局,而是通过局部最优去推出全局最优
这里的核心思想就是利用了摆动序列的特性,一正一负,可以理解为上升和下降的趋势,我们用两个变量up 和down来记录这两个趋势,如果我们发现cur大于pre,那就是up=down+1,如果发现cur<pre,那就是下降趋势down=up+1
这里为什么是up=down+1 down=up+1呢? 因为我们要知道我们的目标是找摆动序列,也就是一正一负,一上一下,那么你刚刚发现了一个上升趋势,他当然要接在下降趋势后面,才是摆动嘛,同理,得出down=up+1,这样,最后我们只需要比较up 和 down哪一个大,哪个就是最大的摆动子序列


真正理解贪心算法这样做后,真实最简单快速的方法
"""
from typing import List
class Solution():
    def wiggleMaxLength(self,nums:List[int])->int:
        if len(nums)<2: 
            return len(nums) 
        # 初始化up 和 down
        up=down=1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>0:  # 上升趋势
                up=down+1
            elif nums[i]-nums[i-1]<0: # 下降趋势
                down=up+1
        return max(up,down)

