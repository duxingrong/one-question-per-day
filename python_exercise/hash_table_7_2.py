"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1: 输入: s = "anagram", t = "nagaram" 输出: true

示例 2: 输入: s = "rat", t = "car" 输出: false

说明: 你可以假设字符串只包含小写字母。
哈希表的核心思想，即通过一个快速的映射机制来存储和访问数据
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 初始化一个大小为26的列表，用于记录字符'a'到'z'的出现次数
        # 列表中的每个元素初始值为0，因为ASCII码中'a'的值为97，所以使用ord('a')作为基准
        record = [0] * 26

        # 遍历字符串s中的每个字符
        for i in s:
            # 计算字符i在字母表中的索引，通过减去'a'的ASCII值
            # 然后使用这个索引在record列表中对应的位置加1，记录字符出现的次数
            # ord(i)是获取字符i的ASCII值
            record[ord(i) - ord("a")] += 1

        # 遍历字符串t中的每个字符
        for i in t:
            # 与s中的字符处理相同，但是这次是减1
            # 因为我们需要检查s和t中每个字符出现的次数是否相同
            record[ord(i) - ord("a")] -= 1

        # 遍历record列表，检查是否有任何元素的值不为0
        # 因为如果所有字符出现的次数都相同，那么减去后应该都是0
        for i in range(26):
            # 如果发现有不为0的元素，说明s和t中至少有一个字符出现的次数不匹配
            # 因此，它们不是变位词，返回False
            if record[i] != 0:
                return False

        # 如果所有字符的出现次数都匹配，即record列表中的所有元素都是0
        # 那么s和t是变位词，返回True
        return True

s='anagram'
t='nagaram'
solution=Solution()
is_anagram=solution.isAnagram(s,t)
print(is_anagram)
