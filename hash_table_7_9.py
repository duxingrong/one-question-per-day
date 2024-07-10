"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意： 答案中不可以包含重复的三元组。

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]

满足要求的三元组集合为： [ [-1, 0, 1], [-1, -1, 2] ]
"""
from typing import List
class Solution():
    def threeSum(self,nums:List[int])->List[List[int]]:
        nums.sort()
        result=[]
        
        for i in range(len(nums)):
            if nums[i]>0:
                return result
            if i>0 and nums[i]==nums[i-1]:    #对a进行去重
                continue
            left=i+1
            right=len(nums)-1
            while right>left:    #不能等于，因为等于的话，说明b=c，就不是三数之和了
                sum=nums[i]+nums[right]+nums[left]
                if sum>0:   #说明c大了
                    right-=1
                elif sum<0:
                    left+=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                #要在得到一组后进行要进行去除，将与得到的相同的b,c都去掉，然后再正常的继续移动指针，将剩下的b,c找到
                    while right>left and nums[right]==nums[right-1]:
                        right-=1        #对c去重
                    while right>left and nums[left]==nums[left+1]:
                        left+=1          #对b去重
                    
                    right-= 1
                    left+= 1       
        
        return result

nums = [-1, 0, 1, 2, -1, -4]
solution=Solution()
result=solution.threeSum(nums)
print(result)
                    