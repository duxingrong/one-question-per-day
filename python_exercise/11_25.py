"""

有效的山脉数组:
给定一个整数数组arr，如果它是有效的山脉数组就返回true,否则返回false

条件：
arr.length>=3
在0<i<arr.length-1的条件下，存在i使得:
arr[0]<arr[1]<...arr[i-1]<arr[i]
arr[i]>arr[i+1]>...arr[arr.length-1]

判断是山峰，就要严格的保证左边到中间，和右边到中间是递增的
可以使用双指针，left和right相遇了就是山峰
如果发现相遇的时候,left和right有一个没有移动，那就说明是一个单调的数组，依旧不是山峰
"""

from typing import List

class Solution():
    def validMountainArray(self,nums:List[int])->bool:
        left = 0
        right = len(nums)-1
        while left<len(nums)-1 and nums[left]<nums[left+1]  :
                left+=1
        while  right>0 and  nums[right]<nums[right-1] :
                right-=1
        return left ==  right  and left!= 0  and right!= len(nums)-1





















