"""
寻找两个正序数组中的中位数

给定两个大小分别为m和n的正序(从小到大)数组nums1和nums2,请你找出并返回这两个正序数组中的中位数

时间复杂度O(log(m+n))

nums1 = [1,3]
nums2 = [2]
合并数组=[1,2,3],中位数2

这个题目真绝了,我们的目的就是找中位数,最通常的方法就是合并数组后,如果数组是奇数,就是第m+n/2个元素,如果数组是偶数,就是m+n/2 和(m+n/2)+1的平均值

所以我们现在的目的是如果在不真的合并数组的前提下将数组分成两部分
加入分割数组,其中在nums1上的是i,在nums2上的是j

左半边数组是 nums1[:i]+nums2[:j]
右半边数组是 nums1[i:]+nums2[j:]长度也为(m-i)+(n-j)

那么可以有公式, i+j = (m+n+1)/2
这里之所以加1是为了满足总长度为奇数,那就左边数组多一个,到时候中位数就是左边数组的最大值
j = (m+n+1)//2 - i

现在问题转化为求出合适的分割点i，使得 nums1[i-1]<=nums2[j] nums2[j-1]<=nums1[i]
满足这两个条件说明我们真的成功将合并数组分成了
1. 左边的元素都小于右边
2. 两边的元素长度几乎一样长
从而就可以快速的写出中位数为多少
"""

from typing import List

class Solution():
    def findMedianSortedArrays(self,nums1:List[int],nums2:List[int])->float:
        #在短的数组上进行二分法,更快
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1

        left = 0        
        right = len(nums1)

        while right>=left:
            i = (left+right)//2
            j = (len(nums1)+len(nums2)+1)//2 -i

            #情况一：i太大了
            if i>0 and nums1[i-1]>nums2[j]:
                right = i-1
            #情况一：i太小了
            elif i<len(nums1) and nums2[j-1]>nums1[i]:
                left = i+1
            else: #这里即包括i=0 i=len(nums1) 以及真的nums1[i-1]<=nums2[j] nums2[j-1]<=nums1[i]
                if (len(nums1)+len(nums2))%2==1: 
                    #总长度为奇数,就是左边数组的最大值
                    return max(nums1[i-1] if i>0 else float('-inf') ,nums2[j-1] if j>0 else float('-inf'))
                else:
                    #总长度为偶数,就是最边最大值和右边最小值/2
                    left_max = max(nums1[i-1] if i>0 else float('-inf') ,nums2[j-1] if j>0 else float('-inf'))
                    right_min = min(nums1[i] if i<len(nums1) else float('inf'),nums2[j] if j<len(nums2)else float('inf'))
                    return (left_max+right_min)/2

        return -1 #代码执行不到这里

if __name__=="__main__":
    nums1 = [1,3]
    nums2 = [2]
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1,nums2))
   







