"""
凌濛水找零
一杯5美元,一次购买一杯,会给你支付5,10,20美元,你必须正确找零,一开始你手上没有任何零钱,如果你可以正确找零,返回True,否则,返回False
"""


"""
我们要清楚我们的返回是什么,是一个True和False,
所以我们的重点是放在哪里呢?我们应该记录我们手上的5和10美元,因为这才是重点,你给别人找钱用不到20美元,所以压根不用管20
然后按照逻辑走,优先级是使用10美元找零
"""
from typing import List
class Solution():
    def lemonadeChange(self,bills:List[int])->bool:
        # 初始化
        five=0
        ten=0
        for val in bills:
            if val==5:  #拿来吧你
                five+=1
            elif val==10: # 需要5美元找零,没有就False
                five-=1
                if five<0:
                    return False
                ten+=1
            else:    ## 需要10和5美元找零,没有就3张5美元,还没有就False
                if ten>0:
                    ten-=1
                    five-=1
                else:
                    five-=3
                if five<0:
                    return False
        return True
                
