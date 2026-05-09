"""
第k小数对和

给你两个升序数组：
nums1 nums2 
请你返回所有数对：

(nums1[i],nums2[j]) 的和里面第k小的值

"""

import heapq

def kth_smallest_pair_sum(nums1, nums2, k):
    
    heap = []

    m  =len(nums1)
    n = len(nums2)

    # 每一行先放第一个元素: nums1[i] + nums2[0]
    for i in range(min(m,k)):
        sub_sum = nums1[i] + nums2[0]
        heapq.heappush(heap,(sub_sum,i,0))

    
    # 弹出来前k-1个小
    for _ in range(k-1):
        cur_sum , i, j = heapq.heappop(heap)

        # 同一行的下一个数对
        if j+1 < n : 
            new_sum = nums1[i] + nums2[j+1]
            heapq.heappush(heap,(new_sum,i,j+1))

    
    # 堆顶就是第K个
    return heap[0][0]

if __name__ == "__main__":
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 5

    print(kth_smallest_pair_sum(nums1, nums2, k))