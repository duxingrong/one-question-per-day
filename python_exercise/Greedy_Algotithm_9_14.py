"""
给定一个整数数组A,我们只能用以下方法修改该数组:我们选择某个索引i并将A[i]替换为-A[i],然后总共重复这个过程k次(可以多次选择同一个索引)
以这种方式修改数组后,返回数组可能的最大和
"""


"""
遍历到i时候,怎么知道该不该替换呢?(保证数组最大值)
那就是先对数组进行排序,如果这样我们最先遇到的负数反转后就是最大的,就可以,如果是发现k有剩余,那就是重新排序,然后k为奇数,取反,为偶数,不管直接返回sam(nums)
"""
from typing import List

class Solution():
    def largestSumAfterKNegations(self,nums:List[int],K:int)->int:
        # 首先进行排序
        nums=sorted(nums)
        for i in range(len(nums)):
            if nums[i]<0 and K>0:
                nums[i]=-nums[i]
                K-=1
        if K%2==1:
            nums=sorted(nums)
            nums[0]=-nums[0]
        return sum(nums)



"""
用最小堆的话会更快
"""
import heapq
class Solution1():
    def largestSumAfterKNegations(self,nums:List[int],K:int)->int:
        # 排序直接换成最小堆
        heapq.heapify(nums)
        while K:
            min_num=heapq.heappop(nums)
            if min_num>=0 and K%2==1:
                heapq.heappush(nums,-min_num)
                break
            elif min_num>=0 and K%2==0:
                heapq.heappush(nums,min_num)
                break
            else:
                heapq.heappush(nums,-min_num)               
                K-=1
                
        return sum(nums)

