"""
在排序数组中查找元素的第一个和最后一个位置

给定一个按照升序排列的整数数组nums,和一个目标值target，找出给定目标值在数组中的开始位置和结束位置
如果数组中不存在目标值target，返回[-1,-1]

要求:时间复杂度O(logn)
"""

from typing import List

class Solution():
    def searchRange(self,nums:List[int],target)->List[int]:
        result = [-1,-1]
        #特殊情况
        if len(nums)==1 and nums[0]==target:
                return [0,0]

        flag = False
        for i in range(len(nums)):
            if nums[i]==target and not flag:
                result[0],result[1]=i,i
                flag =True
            elif nums[i]==target and flag:
                result[0]=min(result[0],i)
                result[1]=max(result[1],i)

            if i>0 and nums[i-1]==target and nums[i]!=target:
                break

        return result



if __name__=="__main__":
    nums = [2,2]
    target = 2
    solution=Solution()
    print(solution.searchRange(nums,target))
