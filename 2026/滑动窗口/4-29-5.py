"""
最多翻转 K 个 0 后的最长连续 1

给你一个只包含0和1的数组nums,以及一个整数k

你最多可以把 k 个 0 翻转成 1

请你返回：翻转最多 k 个 0 后，数组中能够得到的最长连续 1 的长度

"""

"""
窗口时什么？ -> 窗口是包含k个0 的最长连续1的长度
窗口维护什么？ -> 窗口维护的是0个个数
窗口什么时候合法？ -> 0的个数<=k 
什么时候移动left? -> 0的个数> k 的时候
"""

def longest_ones(nums: list[int], k: int) -> int:
    """窗口中维护的就是0的个数"""

    ans = 0 # 维护结果
    count_0 = 0 # 窗口中0的个数
    left = 0 # 左指针

    for right in range(len(nums)):

        # 先加入
        if nums[right]==0: 
            count_0 +=1 

        # 不合法
        while count_0 > k :
            if nums[left]==0:
                count_0 -=1
            left+=1
            
        ans = max(ans, right-left+1)

    return ans 

if __name__=="__main__":
    nums =[1, 1, 0, 1, 1, 1, 0, 1]
    k = 1 
    print(longest_ones(nums,k))