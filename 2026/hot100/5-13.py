"""
字母异位词组

给你一个字符串数组，请你将字母异位词组合在一起。可以按照任意顺序返回结果列表

输入：

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

输出：

[["bat"],["nat","tan"],["ate","eat","tea"]]


两个核心的思路，如何判断两个字符是不是字母异位词? --> 最简单的方法就是排序
然后用哈希表将同类的词语记住就好

甚至不需要两两比较

"""


from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s)) # sorted 返回的不是字符串，是一个列表
            hashmap[key].append(s)

        return list(hashmap.values())

