"""
给你一个按非递减顺序排序的整数数组 nums返回每个数字的平方组成的新数组,要求也按非递减顺序排序。
示例 1
输入nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]，排序后，数组变为 [0,1,9,16,100]
"""


from typing import List

class Solution():
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, i = 0, len(nums) - 1, len(nums) - 1
        res = [float('inf')] * len(nums)  # 列表初始化：[...] * len(nums)是Python中的列表乘法操作，它将中括号内的元素（这里是float('inf')）复制len(nums)次，创建一个新的列表。因此，如果nums的长度是5，那么res将会是[float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
        while l <= r:
            if nums[l] ** 2 < nums[r] ** 2:  # 比较平方大小
                res[i] = nums[r] ** 2
                r -= 1  # 右指针向左移动
            else:
                res[i] = nums[l] ** 2
                l += 1  # 左指针向右移动
            i -= 1  # 结果列表指针向前移动
        return res
# 测试用例
if __name__ == "__main__": #Python的常规用法，当该脚本作为主程序运行时执行下面的代码块。
    solution = Solution()   #创建Solution类的一个实例
    test_nums = [-4, -1, 0, 3, 10]
    print("Input:", test_nums)
    print("Output:", solution.sortedSquares(test_nums)) #调用sortedSquares方法，并打印输出结果。



