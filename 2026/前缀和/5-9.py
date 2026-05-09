"""

正整数数组的第K大子数组和

给你一个只包含正整数的数组nums,以及整数k,请你返回所有非空连续子数组和中第k大值

由于全是正数，所以前缀和肯定是越后越大


不枚举所有子数组和，而是利用正整数数组的单调性，用堆一个一个生成“下一个最大候选”

"""


import heapq

def kth_largest_positive_subarray_sum(nums, k):
    
    n=len(nums)
    prefix = [0]*(n+1)

    # 前缀和
    for i in range(n):
        prefix[i+1] = prefix[i] + nums[i]

    
    heap = []

    # 先把每一个左端点的最大区间和加入堆

    for i in range(n):
        j =n # 是整数数组，以i开头，结尾为结尾的区间是最大值
        sub_sum = prefix[j] - prefix[i]
        heapq.heappush(heap,(-sub_sum,i,j))

    # 然后我们把最大的k-1个值弹出去，再把他们的备选加入进来
    for _ in range(k-1):
        _ , i, j = heapq.heappop(heap)

        new_j = j-1 

        if new_j > i :
            new_sum = prefix[new_j] - prefix[i]
            heapq.heappush(heap,(-new_sum,i,new_j))

    
    # 结束后，堆顶就是第k大
    return -heap[0][0]


if __name__=="__main__":

    nums = [1, 2, 3]
    k = 4
    print(kth_largest_positive_subarray_sum(nums,k))