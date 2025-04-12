from typing import List
class Solution:
    """
    摆动序列
    给你一个数组nums,返回nums中作为摆动序列的最长子序列的长度
    """
    def wiggleMaxLength(self,nums:List[int])->int:
        """
        关键在于上升和下降的趋势
        Args:
            nums: 数组
        Returns:
            最长摆动自序列长度
        """
        low = 1 
        up  = 1 
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                low= up+1
            elif nums[i]<nums[i-1]:
                up= low+1
            else:
                pass
        return max(up,low)


        

