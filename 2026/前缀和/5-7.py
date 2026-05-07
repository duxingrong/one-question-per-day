"""

给你一个整数数组nums ,以及若干个查询queries

每个查阅是一个二元组[left,right],表示询问数组中从下标left 到下标 right 这一段的元素和。

请你返回每个查询对应的区间和


区间 [left, right] 的和 = prefix[right + 1] - prefix[left]
"""


def range_sum(nums, queries):
    prefix = [0] * (len(nums) + 1)

    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]

    ans = []

    for left, right in queries:
        value = prefix[right + 1] - prefix[left]
        ans.append(value)

    return ans


if __name__=="__main__":

    nums = [2, -1, 3, 5, -2, 4]

    queries = [
        [0, 2],
        [1, 4],
        [3, 5],
        [0, 5]
    ]

    print(range_sum(nums,queries))

    

