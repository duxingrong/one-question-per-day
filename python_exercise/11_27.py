"""
移动零

给定一个数组nums,编写一个函数将所有0移动到数组的末尾，同时保持非零元素的相对顺序

输入 ：[0,1,0,3,12]
输出 : [1,3,12,0,0]
必须在原数组上操作，不能拷贝额外的数组,尽量减少操作次数


数组一般这种变换顺序的题目，感觉一定和双指针托不了关系，这题目也确实巧妙
我们用fast = 0 slow =0 
只要fast!=0,就将值赋给slow,如果fast==0,跳过不处理

"""

from typing import List

class Solution():
    def moveZeroes(self,nums:List[int]):
        slow = 0
        fast = 0
        while fast<len(nums):
            if nums[fast]!=0:
                nums[slow],nums[fast] = nums[fast],nums[slow] #交换，甚至比起赋值更简单,少了一步将range(slow,len(nums))赋值0的步骤
                slow+=1
            fast+=1

