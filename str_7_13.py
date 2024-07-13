"""
给定一个字符串，逐个翻转字符串中的每个单词。

示例 
输入: "the sky is blue"
输出: "blue is sky the"
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        # 删除前后空白，默认去掉前后空白
        s = s.strip()  
        # 反转整个字符串
        s = s[::-1]     #s[start:stop:step]   开始，结束，步长，
        # 将字符串拆分为单词，并反转每个单词
        s = ' '.join(word[::-1] for word in s.split())   #分割时默认空格为分隔符
        return s
s='hello world '
print(s)
solution=Solution()
new_s=solution.reverseWords(s)
print(new_s)