"""
3. 无重复字符的最长子串

给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度

"""

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        hashmap = defaultdict(int)
        ans = 0 
        left = 0 

        for right in range(len(s)):

            # 判断
            while hashmap[s[right]] != 0 : # 说明重复
                hashmap[s[left]] -=1
                left +=1 

            # 更新结果
            ans = max(ans, right-left+1)

            # 加入
            hashmap[s[right]] +=1 

        return ans 