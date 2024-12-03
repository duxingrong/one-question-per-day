"""
探索插入位置

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引，如果目标值不存在在数组中，返回它将会被按顺序插入的位置

你可以假设数组中无重复元素

"""

"""
首先要知道一共有多少种情况
1. target比所有的数字都小，加到数组最左边
2. target比所有的数字都大，加到数组最右边
3. target在数组中找到了，直接返回下标i
4. target在数组中要插入，即区间到最小后，left和right越界了
"""

"""
用for循环法
对于该暴力法，只要注意一点，134都可以总结为
if nums[i]>=target:
    return i

对于2,return i = len(nums)
"""

from typing import List

class Solution():
    def searchInsert(self,nums:List[int],target:int)->int:
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)



"""
一盘排序数组，找target，这已经是明牌二分法了
这里我们需要理解，我们二分法使用的是向下整除,所以我们这个区间如果是偶数的话，比如[2,4],如果target<2,那么right=middle-1,应该返回left或者right+1
如果target>2，那么区间压缩成[4]，此时target>4,left=middle+1 right = 0 返回left或者right+1,target<4,right = middle-1 ,left = 0 ,返回left 或者right+1

所以综合下来，除了直接找到返回i之外，其他三种情况都返回同一个值，left或者right-1
"""

class Solution1():
    def searchInsert(self,nums:List[int],target:int)->int:
        left =0 
        right=len(nums)-1
        while left<=right:
            middle = (left+right)//2
            mid_val = nums[middle]
            if mid_val>target: 
                right = middle-1
            elif mid_val<target:
                left = middle+1
            else:
                return middle
        #其他情况都返回right+1或者Left
        return left





