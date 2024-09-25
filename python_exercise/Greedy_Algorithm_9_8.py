"""
你要给孩子们分发饼干,每个孩子最多只能给一块饼干,对每个孩子i,都有一个胃口值g[i],这是能让孩子们满足胃口的饼干的最小尺寸,并且每块饼干j,都有一个尺寸s[j].如果s[j]>=g[j].我们可以把这个饼干j分给孩子i,这个孩子就会得到满足.你的目标是尽可能满足越多数量的孩子,并输入这个最大数值
g=List[int] : 每个孩子的满意度
s=List[int] : 你的饼干值
返回: int (让几个孩子得到了满足)
"""

from typing import List
class Solution():
    def findContentChildren(self,g:List[int],s:List[int])->int:
        result=0
        # 排序
        g= sorted(g)
        s= sorted(s)
        while s and g:
            if s[-1]>=g[-1]:
                s.pop()
                g.pop()
                result+=1
            else:
                g.pop()
        return result
