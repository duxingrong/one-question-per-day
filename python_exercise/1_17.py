"""
87.扰乱字符串
使用下面描述的算法可以扰乱字符串s得到字符串t:
1. 如果字符串的长度为1,算法停止
2. 如果字符串的长度>1,执行下述步骤:
    - 在一个随机下标处将字符串分割成两个非空的子字符串.即,如果已知字符串s,即可以将其分成两个字符串x和y,且满足s = x+y.
    - *随机* 决定是要[交换两个字符串]还是要[保持这两个字符串的顺序不变].即,在执行这一步骤后,s可能是s=x+y或者s=y+x
    - 在x和y这两个字符串上继续从步骤1开始递归执行此算法。

给你两个长度相等的字符串s1和s2,判断s2是否是s1的扰乱字符串，如果是，返回true;否则，返回false

这里同样是递归+动态规划，不会动态规划可以用cache来平替
递归这里就是，我们只能通过长度和字符频率来确定他不是，返回false,以及通过完全相等来判断是扰乱字符串，其他情况就需要使用递归继续拆解来确定
"""

from functools import cache
from collections import Counter
class Solution:
    def isScramble(self,s1:str,s2:str)->bool:
        @cache
        def helper(s1,s2)->bool:
            if s1==s2:
                return True
            if len(s1)!=len(s2):
                return False
            if Counter(s1)!=Counter(s2): # 使用Counter 比较字符频率
                return False

            n = len(s1)
            # 开始递归判断是否是扰乱字符串
            for i in range(1,n): # 这里是防止右边为空字符串
                # 不交换
                if helper(s1[:i],s2[:i]) and helper(s1[i:],s2[i:]):
                    return True
                # 交换
                if helper(s1[:i],s2[-i:]) and helper(s1[i:],s2[:n-i]): # [-i:] 从末尾往前数第i个字符
                    return True

            return False

        return helper(s1,s2)
               



        
