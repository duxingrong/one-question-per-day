"""
题意：给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例： 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。 满足要求的四元组集合为： [ [-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2] ]
"""
from typing import List
class Solution():
    def fourSum(self,nums:List[int],target:int)->List[List[int]]:
        result=[]    #定义一个空列表来存放得到的元组
        nums.sort()  #排序
        for i in range(len(nums)):
            if nums[i]>target and nums[i]>0 and target>0:  #这里这个target>0有必要吗？
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]>target and target>0:    #同理，这里>0有必要吗？
                    break
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left=j+1
                right=len(nums)-1
                while right>left:
                    sum=nums[i]+nums[j]+nums[left]+nums[right]
                    if sum>target:
                        right-=1
                    elif sum<target:
                        left+=1
                    else:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        while right>left and nums[right]==nums[right-1]:
                            right-=1
                        while right>left and nums[left]==nums[left+1]:
                            left+=1
                        right-=1
                        left+=1
        return result

nums = [1, 0, -1, 0, -2, 2]
target = 0
solution=Solution()
result=solution.fourSum(nums,target)
print(result)



