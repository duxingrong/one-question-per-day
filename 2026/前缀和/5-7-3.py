"""
和至少为k的最短子数组

给你一个整数数组nums和一个整数k,请你返回：

和至少为k的最短非空连续子数组的长度

如果不存在这样的子数组，返回-1.


prefix[j] - prefix[i] >= k 
即：
prefix[i] <= prefix[j] - k 同时我们还希望j-i 尽量小 ,由j固定,也就是i尽量大
"""

from collections import deque

def shortest_subarray(nums, k):
    n = len(nums)

    # prefix[j] 表示 nums[0:j] 的和
    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    ans = float("inf")
    dq = deque()  # 存的是 prefix 的下标，不是 prefix 的值

    for j in range(n + 1):
        # 队头是当前最小的 prefix[i]
        # 如果 prefix[j] - prefix[dq[0]] >= k，说明找到一个可行子数组
        while dq and prefix[j] - prefix[dq[0]] >= k:
            ans = min(ans, j - dq.popleft())

        # 如果当前 prefix[j] 更小，并且 j 更靠右
        # 那么旧的队尾就不可能比当前 j 更优
        while dq and prefix[j] <= prefix[dq[-1]]:
            dq.pop()

        # 当前 j 作为未来的候选左端点
        dq.append(j)

    return ans if ans != float("inf") else -1

if __name__ == "__main__":
    nums = [2, -1, 2]
    k = 3
    print(shortest_subarray(nums,k))