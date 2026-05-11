"""
有序矩阵中第k小的元素

给你一个n x n 矩阵 matrix ，满足

每一行从左到右升序
每一列从上到下升序

请你返回矩阵中第k小的元素


"""

import heapq

def kth_smallest_in_matrix(matrix, k):
    """多条有序序列，每一行入堆"""

    n = len(matrix) # 一共有多少行
    cols = len(matrix[0])
    heap = [] # 堆

    # 每一行第一个元素先入堆  
    for row in range(min(n,k)):  # 只放前 k 行，是因为第 k 行及之后的第一个元素，前面至少已经有 k 个元素不大于它。所以它们不可能成为第 k 小。
        heapq.heappush(heap,(matrix[row][0],row,0))

    # 弹出k-1个小的
    for _ in range(k-1):
        value , row, col = heapq.heappop(heap)

        # 加入同一行的下一个元素
        if col +1 < cols : 
            heapq.heappush(heap,(matrix[row][col+1],row,col+1))

    return heap[0][0]



if __name__ == "__main__":
    matrix = [
        [1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ]

    k = 8

    print(kth_smallest_in_matrix(matrix, k))