"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并原地修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1: 给定 nums = [3,2,2,3], val = 3, 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。 你不需要考虑数组中超出新长度后面的元素。

示例 2: 给定 nums = [0,1,2,2,3,0,4,2], val = 2, 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 4, 0, 3
"""                 
#之前做过
# from typing import List
# class Solution():
#     def removeElements(self,nums:List[int],val:int)->int:
#         #初始指针
#         k=0
#         for  i in nums:
#             if nums[i]!=val:
#                 nums[k]=nums[i]
#                 k+=1
#         return k
# nums=[3,2,2,3]
# val=3
# solution=Solution()
# length=solution.removeElements(nums,val)
# print(length)
# print(nums[:length])

"""
双向双指针法,时间复杂度o(n)，空间复杂度o(1)
"""
from typing import List
class Solution():
    def removeElements(self,nums:List[int],val:int)->int:
        #初始化双指针
        l=0
        r=len(nums)-1
        #开始遍历
        while l<=r:
            while l<=r and nums[l]!=val :    #l指针遇到val才停止
                l+=1
            while l<=r and nums[r]==val:     #r指针遇到非val才停止
                r-=1
            if l<r:
                nums[l],nums[r]=nums[r],nums[l] #这是交换，刚好可以把val换去右边，非val换到左边
        return l        #left移动一次，就会多一个非val 因为left从0开始
nums=[0,1,2,2,3,0,4,2]
val=2
solution=Solution()
length=solution.removeElements(nums,val)
print(length)
print(nums[:length])
            
                            
            


