"""
第k小乘法表数字

给你两个整数m和n,表示一个mxn的乘法表

第i行第j列的值为: i*j 

其中:

1<= i <= m 
1<= j <= n 

请你返回这个乘法表中第k小的数字
"""

import heapq

def kth_smallest_multiplication_table(m, n, k):
    
    heap = []
    cols = n 

    # 每一行第一个元素先加入
    for row in range(min(m,k)):
        heapq.heappush(heap,((row+1)*1,row,0))

    # 剔除掉k-1个小的
    for _ in range(k-1):
        _ , row ,col = heapq.heappop(heap)

        if col +1 < cols :
            heapq.heappush(heap,((row+1)*(col+1+1),row,col+1))

    return heap[0][0]

if __name__ == "__main__":
    m = 2
    n = 3
    k = 6

    print(kth_smallest_multiplication_table(m,n,k))