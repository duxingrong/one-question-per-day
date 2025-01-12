"""
寻找两个正序数组的中位数

给定两个大小分别为m和n的正序(从小到大)数组nums1和nums2。请你找出并返回正序数组的中位数。

算法的时间复杂度应该为olog(m+n)

这道题目，它寻找两个数组的中位数，正常肯定是将两个数组融合排序然后寻找。但是我们可以通过假装融合的方法来寻找，只需要将所有数字分成两分就好

假设nums1的索引为i, 则分成nums1[:i],nums1[i:]
假设nums2的索引为j, 则分成nums1[:j],nums1[j:]
则有 i+j = m+n+1-i-j 这里减1是为了凑整数
i确定了，j也就确定了
所以我们就是遍历所有i用二分法找出这个恰当的i，j,使得刚好分成,也就好求出中位数
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self,nums1:List[int],nums2:List[int])->float:

        ## 首先确定nums1长度短
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1

        ## 变量
        m = len(nums1)
        n = len(nums2)
        left = 0
        right = m
        ## 二分法最快求出i
        while left <=right:

            i = (left+right)//2
            j = (m+n+1)//2 - i

            ## 边界处理，如果i或者j为0和m，n，那就会越界，这个时候根据情况将边界值变成无穷
            nums1_left_max = float('-inf') if i==0 else nums1[i-1]
            nums1_right_min = float('inf') if i==m else nums1[i]
            nums2_left_max = float('-inf') if j==0 else nums2[j-1]
            nums2_right_min = float('inf') if j==n else nums2[j]

            ## 判断是否刚好合适
            if nums1_left_max<=nums2_right_min and nums2_left_max<=nums1_right_min:
                ## 判断是偶数还是奇数，从而求中位数
                if (m+n) %2 == 1:
                    return max(nums1_left_max,nums2_left_max)
                else:
                    return ((max(nums1_left_max,nums2_left_max))+min(nums1_right_min,nums2_right_min))/2
            elif nums1_left_max>nums2_right_min: ## 说明i偏大了
                right = i-1
            elif nums2_left_max>nums1_right_min: ## 说明i偏小了
                left = i+1

        raise ValueError("Input arrays are not valid")
                    
            
        
if __name__=="__main__":
    s = Solution()
    # 测试用例
    print(s.findMedianSortedArrays([1, 3], [2]))  # 输出: 2.0
    print(s.findMedianSortedArrays([1, 2], [3, 4]))  # 输出: 2.5
    print(s.findMedianSortedArrays([0, 0], [0, 0]))  # 输出: 0.0
    print(s.findMedianSortedArrays([], [1]))  # 输出: 1.0
    print(s.findMedianSortedArrays([2], []))  # 输出: 2.0





























