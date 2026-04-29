"""题目：最长“可修复”连续子数组

给你一个整数数组 nums 和一个整数 k。

你可以最多修改 k 个元素。每次修改可以把数组中的一个元素改成任意整数。

请你返回：经过最多 k 次修改后，数组中能够形成的最长连续相等子数组的长度。

示例 1
nums = [1, 2, 2, 1, 2, 2, 2]
k = 1

输出：6

解释：
把第 4 个元素 1 改成 2，数组变成：

[1, 2, 2, 2, 2, 2, 2]

最长连续相等子数组长度是 6。

示例 2
nums = [1, 3, 3, 3, 2, 3, 1, 3]
k = 2

输出：7

解释：
把 2 和 1 都改成 3，整个数组都可以变成连续相等。

示例 3
nums = [1, 2, 3, 4, 5]
k = 1

输出：2

输入范围
1 <= len(nums) <= 2 * 10^5
0 <= k <= len(nums)
-10^9 <= nums[i] <= 10^9
要求

请你写一个函数：
def longest_equal_subarray_after_change(nums: list[int], k: int) -> int:
    pass

要求时间复杂度尽量做到：O(n)

空间复杂度：O(n)"""

"""
首先要能想到，我们就是在找一个最长的窗口，保证其中的窗口长度-窗口中最多的相同数后的值<=k的话，说明这个窗口可修复

然后暴力解法就是

for left in range(len(nums)):
    for right in range(left,len(nums)):
        统计nums[left:right+1] 里的众数次数
        判断是否合法

        
再想到我们维护的是一个滑动窗口

right 是探索者，负责一直往右尝试扩大窗口
left 是修正者，窗口太大、不合法时才往右收缩
ans 是记录员，记录历史上出现过的最大合法窗口
"""


from collections import defaultdict

def longest_equal_subarray_after_change(nums: list[int], k: int) -> int:
    """找到一个最大窗口，实现窗口长度 - max_count <= k """

    count = defaultdict(int)
    left = 0
    max_count = 0 
    ans = 0 

    for right in range(len(nums)):
        x = nums[right]
        count[x]+=1 
        max_count = max(max_count,count[x])
        
        while right -left + 1 - max_count > k:
            count[nums[left]]-=1 
            left +=1 
        
        ans = max(ans,right-left+1)

    return ans 
             

if __name__ == "__main__":
    nums = [1, 3, 3, 3, 2, 3, 1, 3]
    k = 2 
    ans = longest_equal_subarray_after_change(nums,k)

    print(ans)
