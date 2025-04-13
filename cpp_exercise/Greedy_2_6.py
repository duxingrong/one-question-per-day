from typing import List
class Solution:
    """
    最大子序和
    """
    def maxSubArray(self,nums:List[int])->int:
        """
        如果累加反而没有他本身大，那就说明前面的都是累赘
        """
        sum = 0 # 局部最大值
        result = float('-inf') # 全局最大值

        for num in nums:
            sum = max( sum+num, num)
            result = max(sum,result)

        return int(result)

if __name__ == "__main__":
    solution = Solution()
    # nums= [-2,1,-3,4,-1,2,1,-5,4]
    nums =[-1]
    print(solution.maxSubArray(nums))

