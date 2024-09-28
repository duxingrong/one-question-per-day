"""
给定一个区间的集合,找到需要移除区间的最小数量,使剩下的区间互不重叠
可以认为区间的终点总是大于它的起点,区间[1,2]和[2,3]的边界相互接触,但没有相互重叠
例如:
输入:[[1,2],[1,2],[1,2]]
输出:2 (你需要移除两个[1,2]来使得剩下的区间没有重叠)
"""

"""
第一次思考的话,是排序,然后我们要关注的是现在是按照左边界都排过一次,那么,如果下一个和上一个重叠了,我们要根据他们两个谁的尾巴长来决定删去谁,如果当前的数组的尾巴长,那我们就删掉这个数组,如果是前一个的尾巴拖的更长,就删掉的是前一个元素,这都可以理解为更新了当前i的右边界
"""
from typing import List

class Solution():
    def eraseOverlapIntervals(self,nums:List[List[int]])->int:
        if len(nums)<1:
            return 0
        nums=sorted(nums,key=lambda x:x[0])
        ans=0
        for i in range(1,len(nums)):
            if nums[i][0]<nums[i-1][1]:
                ans+=1
                nums[i][1]=min(nums[i][1],nums[i-1][1])  #这里取最小的边界,可以理解为我们保留的是右边界更小的,因为有边界更小的更不容易影响更后面的数组
        return ans


nums=[[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
solution=Solution()
print(f"需要移除{solution.eraseOverlapIntervals(nums)}个")


