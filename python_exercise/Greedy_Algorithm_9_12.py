"""
跳跃游戏1
给你一个非负整数数组,你最初位于子数组的第一个位置
数组中的每个元素代表你在该位置可以跳跃的最大长度
判断是否可以到达最后一个位置
"""


"""
这个题我们很容易从每一次该跳几步来思考,所以才会感觉难
其实我们只需要注意我们最远的跳跃下标,问题就很简单了(因为我们只需要最远的跳跃范围覆盖了最后一个下标,那就一定可以过去)
那什么情况我们会失败呢？那就是如果我们遍历的这个i>我们之前更新的最大的覆盖范围(cover):因为我们压根不可能到达i这个位置,我们没有方法可以达到,不然cover一定会>=i,这样的话代码逻辑就有了
"""

from typing import List
# while
class Solution():
    def canJump(self,nums:List)->bool:
        if len(nums)==1: # 压根不用跳跃
            return True
        cover=0 # 初始化
        i=0 # 下标从0开始
        while i <= cover:
            if cover>len(nums)-1:
                return True
            cover=max(cover,i+nums[i])
            i+=1
        return False


# for
class Solution1():
    def canJump(self,nums:List):
        if len(nums)==1: # 压根不用跳跃
            return True
        cover=0
        for i in range(len(nums)):
            if i>cover:
                return False
            cover=max(cover,i+nums[i])
            if cover>len(nums)-1:
                return True
           



