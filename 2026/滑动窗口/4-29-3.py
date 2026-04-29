"""

长度最小的子数组

给你一个正整数数组nums 和一个 正整数 target 

请你返回：数组中满足连续子数组之和大于等于target的最短长度

如果不存在这样的子数组，返回0 

时间复杂度：O(n)
空间复杂度：O(1)

"""


"""
最长窗口：不合法时收缩
最短窗口：合法时收缩
"""


def min_subarray_len(target: int, nums: list[int]) -> int:
    """维护一个窗口，里面的和> = target的时候便记录结果"""

    ans = float("inf") # 维护结果
    window_sum = 0 # 维护窗口内的数字的总和
    left = 0 # 左指针

    for right in range(len(nums)):

        # 先加入right
        window_sum += nums[right]

        # 判断条件
        while window_sum >= target:
            ans = min(ans , right-left+1)
            window_sum -= nums[left]
            left+=1 

    return 0 if ans == float("inf") else ans


if __name__=="__main__":
    nums = [2,3,1,2,4,3]
    target = 7 
    print(min_subarray_len(target,nums))

