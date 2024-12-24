"""
下一个排列

实时获取下一个排列的函数,算法需要将给定数字序列重新排列成字典序中下一个更大的排列

如果不存在下一个更大的排列,则将数字重新排列成最小的排列(即升序排列)

必须原地修改,只允许使用额外常数空间

nums = [1,2,3]
输出: [1,3,2]  就是返回用元素组成的比这个数字大的数字的最小值

nums=[3,2,1]
输出: [1,2,3]


这个题目确实有意思
1. 从后向前遍历,找到第一个升序的位置,即nums[i]<nums[i+1] ,因为这里可以确定这个i就是要交换的位置
2. 再次从最后开始遍历,因为此时后面的都是降序,所以找到第一个比i大的数字和i交换,才是最小值
3. 交换后,此时nums[i+1:]也依旧为降序排列,此时反转nums[i+1:]就是最大的最小值

"""

from typing import List
class Solution():
    def nextPermutation(self,nums:List[int])->None:
        
        #第一步,找到交换位置i,第一个升序位置
        i = len(nums)-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1 
        
        #第二步,找到交换位置j,第一个比nums[i]大的元素
        if i>=0:
            j = len(nums)-1
            while nums[j]<=nums[i]:
                j-=1 
            #开始交换
            nums[i],nums[j] = nums[j],nums[i]

        #交换nums[i+1:] 就算上面i=-1,代表是全降序,那也是直接反转
        left = i+1 
        right = len(nums)-1 
        while right>left:
            nums[left],nums[right] = nums[right] , nums[left]
            left+=1 
            right-=1 


 
 

    
    


            