"""
按奇偶排序数组

给定一个非负整数数组A,A中一半整数是奇数，一半整数是偶数

对数组进行排序，以便当A[i]为奇数时，i也是奇数;当A[i]为偶数的时候,i也是偶数

你可以返回任何满足上述条件的数组作为答案

"""



from typing import List

class Solution():
    def sortArrayByParityII(self,nums:List[int]):
        left = 0
        right = 1
        while left< len(nums) and right<len(nums):
            while  left<len(nums) and nums[left]%2==0 :
                left+=2
            while  right<len(nums) and nums[right]%2==1 :
                right+=2
            if left <len(nums) and right<len(nums):
                nums[left],nums[right]=nums[right],nums[left]
                left+=2
                right+=2
        return nums


if __name__=="__main__":
    nums = [4,2,5,7]
    obj = Solution()
    result = obj.sortArrayByParityII(nums)
    print(result)

