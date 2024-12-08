"""
同构字符串

给定两个字符串s和t，判断它们是否是同构的

如果s中的字符可以按某种映射关系替换得道t，那么这两个字符串是同构的.

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

s="egg", t="add" true
s="foo"  t="bar" false
s="paper" t="title" true

可以假设s和t长度一样
"""


#是同构字符串就是需要满足双向唯一映射

from collections import defaultdict

class Solution():
    def isIsomorphic(self,s:str,t:str)->bool:
        #创建字典
        dict1 = defaultdict(str)
        dict2 = defaultdict(str)

        for i in range(len(s)):

            #s对应唯一的t
            if not dict1[s[i]]:
                dict1[s[i]]=t[i]

            #t对应唯一的s
            if not dict2[t[i]]:
                dict2[t[i]]=s[i]

            #不是唯一映射，直接False
            if dict1[s[i]]!=t[i] or dict2[t[i]]!=s[i]:
                return False

        return True




