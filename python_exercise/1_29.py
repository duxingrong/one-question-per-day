"""
220.存在重复元素|||

给你一个整数数组nums和两个整数indexDiff 和 valueDiff

找出满足下述条件的下标对(i,j):
i!=j
abs(i-j)<=indexDiff
abs(nums[i]-nums[j])<=valueDiff

如果存在，返回true ; 否则，返回false

"""

from typing import List
class Solution1:
    def function(self,nums:List[int],indexDiff:int,valueDiff:int)->bool:
        """
        最苯的方法
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(i-j)>indexDiff:
                    break
                if abs(nums[i]-nums[j])<=valueDiff:
                    return True

        return False



from sortedcontainers import SortedList
from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self,nums:List[int],indexDiff:int,valueDiff:int)->bool:

        window = SortedList() # 维护一个有序窗口

        for i in range(len(nums)):
            # 查找窗口中是否有符合条件的数
            left = nums[i]-valueDiff
            right = nums[i]+valueDiff

            # 在窗口中找到元素
            # bisect_left(x) : 找到第一个>=x的元素索引 "左边界"
            # bisect_right(x) : 找到第一个>x的元素索引 "右边界+1"
            if window.bisect_right(right)>window.bisect_left(left):
                return True # 找到了符合条件的元素

            # 把nums[i]加入窗口
            window.add(nums[i])

            # 维持窗口大小
            if i>=indexDiff:
                window.discard(nums[i-indexDiff])

        return False



