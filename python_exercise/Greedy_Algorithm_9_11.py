"""
给定一个数组,他的第i个元素时一支给定股票第i天的价格
设计一个算法来计算你所能获得的最大利润,你可以尽可能的完成更多的交易(多次买卖一支股票)
"""

"""
这题目在做过摆动序列之后简直太明白了,我们其实就是找的上升趋势,当股票涨的时候就卖出去了(这里甚至是事后诸葛亮,你都是在发现上升后才定义你之前买了的)
"""
from typing import List,Optional
class Solution():
    def maxProfit(self,prices:List[int])->Optional[int]:
        if len(prices)<2:
            return None
        result = 0
        for i in range(1,len(prices)):
            if (prices[i]-prices[i-1])>0:
                val =prices[i]-prices[i-1] 
                result+=val
        return result
                
        
