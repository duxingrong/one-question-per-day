"""
题意：给定两个数组，编写一个函数来计算它们的交集。
"""
from typing import List
class Solution:
    # 定义一个方法，用于返回两个数组的交集
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 使用哈希表（字典）存储nums1数组中的所有元素，同时记录每个元素出现的次数
        table = {}
        for num in nums1:
            # 如果字典中已有该元素，则增加其计数，否则设置其计数为1
            table[num] = table.get(num, 0) + 1
        
        # 使用集合来存储最终的交集结果，集合自动去除重复元素
        res = set()
        for num in nums2:
            # 如果当前元素存在于哈希表中，则将其添加到结果集合中
            if num in table:
                res.add(num)
                # 由于集合中不允许有重复元素，一旦添加，就从哈希表中删除该元素
                del table[num]
        
        # 将集合转换为列表并返回，因为集合是无序的，如果需要有序结果，可以对结果进行排序
        return list(res)

nums1=[1,2,3,4,5]
nums2=[1]
solution=Solution()
set=solution.intersection(nums1,nums2)
print(set)