"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1: 输入: haystack = "hello", needle = "ll" 输出: 2

示例 2: 输入: haystack = "aaaaa", needle = "bba" 输出: -1
"""
from typing import List
class Solution:
    #制作一个前缀表的求法
    def getNext(self, next: List[int], s: str) -> None:
        #初始化前缀表
        j = 0
        next[0] = 0
        for i in range(1, len(s)):
            #当不匹配时，需要退回去
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            #相等时，相等前后缀长度加一
            if s[i] == s[j]:
                j += 1
            next[i] = j
    #开始查找
    def strStr(self, haystack: str, needle: str) -> int:
        #判断needle是否为空
        if len(needle) == 0:
            return 0
        #得到前缀表
        next = [0] * len(needle)
        self.getNext(next, needle)
        #开始匹配
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1   #返回的是第一个元素的指针
        return -1
