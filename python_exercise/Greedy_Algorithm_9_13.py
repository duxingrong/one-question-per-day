"""
跳跃游戏2
这一次是假设你不管怎样一定可以到终点,返回的是最少的步骤
"""


"""
这题又是思维上的一点转变
我们还是使用最大覆盖范围
逻辑是:我们记录当前的覆盖范围和下一次的覆盖范围,如果当i=cover时候,我们此时如果还没有到终点,那就必须还要走一次,来更新最大覆盖范围,一次类推,当
目前的cover>len(nums)-1的时候,直接返回次数就行
"""
from typing import List

class Solution():
    def jump(self,nums:List[int])->int:
        if len(nums)==1:
            return 0
        #初始化
        current_cover=0
        next_cover=0
        ans=0
        for i in range(len(nums)):
            # 首先就是看能不能到达终点
            if current_cover>=len(nums)-1:
                break
            # 每次遍历需要更新下一步的能覆盖的最大值
            next_cover=max(next_cover,i+nums[i])
            # 如果遍历到了当前发改范围的最大值,就需要下一步来更新最大范围
            if i==current_cover:
                ans+=1
                current_cover=next_cover
        return ans
            
