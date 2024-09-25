"""
给定一个整数数组nums,找到一个具有最大和的连续子数组(子数组最少包含一个元素),返回其最大和
"""


"""
首先要明确要求,是找到最大的连续子数组和(连续:说明不能跳跃)
最暴力的方法就是找出每一个位置的所有子数组和
现在优化,假如我们现在遍历到了一个i ,得到了一个最大和,我们怎么判断是继续累加?还是从新开始呢?
这里的判断真的很精髓:
我们其实重点没有放在当前nums[i]的正负上面,而是放在了我们之前累加的和上面(这样我们就完全不用管很多的边界条件)
1. 如果我们的当前和它+nums[i]后还小于nums[i]: 说明他就是个废物,应该立刻丢掉包袱,从当前值从新开始
2. 如果我们的当前和它+nums[i]后还大于nums[i]: 说明他是有用的,那就继续叠加
现在的问题就变成了,如果你现在是val=2,然后nums[i]=-1 ,你加上后满足条件1,但是很明显的你val是变小了,所以,我们每一次循环完成后都需要更新全局最大和,这样遍历结束后,自然得到最大值
"""
from typing import List,Optional
class Solution():
    def maxSubArray(self,nums:List[int])->Optional[int]:
        # 特殊情况
        if len(nums)==0:
            return None
        # 初始化局部最大值和全局最大值
        current_sum=maxsum=nums[0]
        for i in range(1,len(nums)):
            if current_sum+nums[i]>=nums[i]:
                current_sum+=nums[i]
            else:
                current_sum=nums[i]
            maxsum=max(current_sum,maxsum)
        return maxsum



