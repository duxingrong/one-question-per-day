"""
给定一个字符串 s 和一个整数 k，从字符串开头算起, 每计数至 2k 个字符，就反转这 2k 个字符中的前 k 个字符。

如果剩余字符少于 k 个，则将剩余字符全部反转。

如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"
"""
from typing import List
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        1. 使用range(start, end, step)来确定需要调换的初始位置
        2. 对于字符串s = 'abc'，如果使用s[0:999] ===> 'abc'。字符串末尾如果超过最大长度，则会返回至字符串最后一个值，这个特性可以避免一些边界条件的处理。
        3. 用切片整体替换，而不是一个个替换.
        """
        
        def reverse_substring(text):
        #定义了一个函数，将text反转
            left, right =  0 ,len(text) - 1
            while left < right:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            return text
        #将s变成链表
        res = list(s)
        #每次取出2k单位来操作
        for cur in range(0, len(s), 2 * k):
            res[cur: cur + k] = reverse_substring(res[cur: cur + k])
        #res[cur: cur + k] 表示从列表 res 中取出从索引 cur 到 cur + k（左闭右开）
        return ''.join(res)
        #"".join()，将序列中的元素连接成单一的字符串
s = "abcdefg"
k = 2
print(s)
solution=Solution()
new_str=solution.reverseStr(s,k)
print(new_str)

