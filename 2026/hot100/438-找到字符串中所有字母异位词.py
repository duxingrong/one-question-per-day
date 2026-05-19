"""
438. 找到字符串中所有字母异位词

给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序

"""

"""
长度固定的滑动窗口
"""

from typing import List 
from collections import Counter ,defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        ans = []
        need = Counter(p)
        window = defaultdict(int)
        left = 0 
        valid = 0 
        
        for right in range(len(s)):
            # 加入
            window[s[right]] +=1 

            # 判断valid 
            if s[right] in need and need[s[right]] == window[s[right]]: 
                valid +=1 

            # 判断长度
            while right - left +1 > len(p):
                 
                if window[s[left]] == need[s[left]]:
                    valid -=1
                window[s[left]] -= 1
                if window[s[left]] == 0: del window[s[left]]
                left +=1

            # 长度刚好满足且条件也满足
            if right-left+1 == len(p) and valid == len(need):
                ans.append(left)  

        return ans 



