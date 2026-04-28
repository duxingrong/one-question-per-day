"""
和为K的连续子数组个数

给你一个整数数组nums和一个整数k

请你返回：数组中连续子数组的和等于k的个数



心路历程：

我想找一段连续子数组和为 k。
一段连续子数组和 = 两个前缀和的差。
所以 current_sum - previous_sum = k。
所以 previous_sum = current_sum - k。
所以我每到一个位置，只要查以前出现过多少个 current_sum - k。

"""

def subarray_sum(nums: list[int], k: int) -> int:
    """维护的是前缀和"""

    current_sum = 0  # 当前前缀和 
    count = {0:1}    # 所有的已遍历的子数组前缀和，开局默认0的前缀和出现了1次
    ans = 0 # 维护结果

    for i in range(len(nums)):
        current_sum += nums[i] 
        prev_sum = current_sum - k 
        ans += count.get(prev_sum,0)
        count[current_sum] = count.get(current_sum,0) + 1 

    return ans


if __name__ == "__main__":
    nums = [1, -1, 0]
    k = 0
    print(subarray_sum(nums, k))  # 3