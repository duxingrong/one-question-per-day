"""
15. 三数之和


给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

"""

"""
经典的做法是排序后使用双指针，此时还需要注意的是减枝
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums = sorted(nums)
        ans = []

        for i in range(len(nums)-2):

            # i 的减枝
            if i > 0  and nums[i] == nums[i-1]:
                continue 
        
            if nums[i] > 0 : break 

            left = i +1 
            right = len(nums)-1 

            while left < right : 
                if nums[i] + nums[left] + nums[right] == 0 :
                    # 记录答案
                    ans.append([nums[i],nums[left],nums[right]])
                    left +=1 
                    right -=1 
                    while left < right and nums[left] == nums[left-1]: 
                        left +=1 
                    while left < right and nums[right] == nums[right+1]:
                        right -=1 
                elif nums[i] + nums[left] + nums[right] > 0 :
                    right -=1 
                else : 
                    left +=1 
            

        return ans 
            


