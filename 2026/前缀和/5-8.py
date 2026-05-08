"""
长度不超过K的最大子数组和

给你一个整数数组nums 和一个整数k ,请你返回：

长度不超过k的非空连续子数组的最大和



"""

from collections import deque

def max_subarray_sum_at_most_k(nums, k):
    
    n = len(nums)
    prefix = [0]*(n+1)

    # 计算前缀和
    for i in range(n):
        prefix[i+1] = prefix[i] + nums[i]

    
    dq = deque()
    ans = float("-inf")

    for j in range(n+1):

        # 判断是否超过长度 j-i <=k 即 j-k > i 时的i需要剔除 必须放在第一步 必须在使用队头更新答案之前，先删除过期下标
        while dq and dq[0] < j-k :
            dq.popleft()

        # 找答案
        if dq :
            ans = max(ans, prefix[j]-prefix[dq[0]]) # 因为是递增数列，所以这个一定是此时最大和

        # 维护递增
        while dq and prefix[j]<= prefix[dq[-1]]:
            dq.pop()

        # 加入 
        dq.append(j)

    return ans 


if __name__ == "__main__":
    nums = [1, -2, 3, 5, -1, 2]
    k = 3
    print(max_subarray_sum_at_most_k(nums,k))