from typing import List
class Solution:
    """
    分发饼干
    """
    def findContentChildren(self,g:List[int],s:List[int])->int:
        """
        Args:
            g: 小朋友的胃口
            s: 饼干的数量
        Returns:
            可以满足的数量 gIndex
        """
        g = sorted(g)
        s = sorted(s)
        gIndex = 0
        for num in s:
            if gIndex<len(g) and num>=g[gIndex]:
                gIndex+=1

        return gIndex
