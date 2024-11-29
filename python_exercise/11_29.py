"""
寻找数组的中心下标

数组的中心下标是数组的一个下标，其左侧的所有元素想加的和等于右侧所有元素相加的和
如果数组有多个中心下标，应该返回最靠左边的那一个，如果数组不存在中心下标，返回-1

nums= [1,7,3,6,5,6]
输出 3
1+7+3 == 5+6

1. 求总和，然后设置变量total_val=0;
2. 遍历数组，先判断(sum-nums[i])%2==0 and  total_val是否等于(sum-nums[i])/2 
3. 是，就返回i,否则，total_val+=nums[i]
4. return -1
"""

from typing import List

class Solution():
    def pivotIndex(self,nums:List[int])->int:
        sum_val =sum(nums)
        current_sum  = 0
        for i in range(len(nums)):
            if (sum_val-nums[i])%2==0 and  current_sum==(sum_val-nums[i])/2:
                return i
            current_sum+=nums[i]
        return -1

nums= [1,7,3,6,5,6]
solution = Solution()
print(solution.pivotIndex(nums))
