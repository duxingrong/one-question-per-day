"""
76. 最小覆盖子串

给定两个字符串 s 和 t，长度分别是 m 和 n，返回 s 中的 最短窗口 子串，使得该子串包含 t 中的每一个字符（包括重复字符）。如果没有这样的子串，返回空字符串 ""。

测试用例保证答案唯一
"""

"""
滑动窗口，然后使用valid
"""

from collections import Counter,defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need = Counter(t)
        window = defaultdict(int)

        left = 0
        valid = 0
        ans = float("inf")
        start = 0 

        for right in range(len(s)):
            # 加入
            window[s[right]]+=1 

            # 判断valid 
            if s[right] in need and window[s[right]]==need[s[right]]:
                valid += 1 

            # 判断是否满足
            while valid == len(need) : 
                if ans > right-left+1:
                    ans = right-left+1
                    start = left 

                if s[left] in need and  window[s[left]] == need[s[left]]:
                    valid -= 1 
                window[s[left]]-=1
                if window[s[left]]==0: del window[s[left]]

                left += 1 

            
        return s[start:start+ans] if ans!=float("inf") else ""

