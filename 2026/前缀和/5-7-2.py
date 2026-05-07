"""
给你一个整数数组nums和一个整数k,请你统计并返回

数组中和等于k的连续子数组个数


"""

def subarray_sum(nums, k):
    """ current_sum -k = prev_sum 主要是维护prev_sum"""

    prev_sum = {0:1}
    current_sum = 0
    ans = 0 

    for i in range(len(nums)):

        current_sum = current_sum + nums[i] 
        
        # 判断能否找到满足条件的Prev_sum 

        if current_sum - k  in prev_sum:
            ans += prev_sum[current_sum-k]

        prev_sum[current_sum] = prev_sum.get(current_sum,0) + 1 

    return ans 


if __name__ == "__main__":

    nums = [1, -1, 1, 1]
    k = 2
    print(subarray_sum(nums,k))