"""

第k大子数组和

给你一个整数数组nums和一个整数k,请你返回

所有非空连续子数组中的第k大值


"""

# 暴力
import heapq

def kth_largest_subarray_sum(nums, k):
    n = len(nums)

    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    heap = []

    for j in range(1, n + 1):
        for i in range(j):
            sub_sum = prefix[j] - prefix[i]
            heapq.heappush(heap, -sub_sum)

    for _ in range(k - 1):
        heapq.heappop(heap)

    return -heapq.heappop(heap)


"""
维护一个大小最多为K的小根堆 堆里保存目前见过的前k大子数组和
"""

import heapq

def kth_largest_subarray_sum(nums, k):
    n = len(nums)

    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    heap = []

    for j in range(1, n + 1):
        for i in range(j):
            sub_sum = prefix[j] - prefix[i]

            if len(heap) < k: # 不足k就直接加入
                heapq.heappush(heap, sub_sum)
            elif sub_sum > heap[0]: # 始终维护k的见到的最大的
                heapq.heapreplace(heap, sub_sum)

    return heap[0] # 由于是小根堆，所以最小的就是第k大


if __name__ == "__main__":
    nums = [1, 2, 3]
    k = 4
    print(kth_largest_subarray_sum(nums,k))
        
