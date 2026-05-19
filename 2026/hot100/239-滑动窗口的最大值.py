"""

239. 滑动窗口最大值

给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 

"""

"""
堆里不仅需要记录数值，还需要记录下标，这样才能更具下标来排除
"""

from typing import List 
import heapq 

class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        ans = []

        for i in range(len(nums)):

            # 加入堆
            heapq.heappush(heap,(-nums[i],i))

            # 更新堆
            while heap and heap[0][1] < i -k +1 : # 说明这个值已经不在窗口内了
                heapq.heappop(heap)


            # 如果长度满足了，求答案
            if i >= k - 1 : 
                ans.append(-heap[0][0])

        return ans 
            


"""
更经典的使用单调栈

只保留有可能成为最大值的元素，且存的是下标

"""

from collections import deque 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        queue = deque()
        ans = []

        for i in range(len(nums)):

            # 当前nums[i]进来之前 ，保证单调
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()

            # 当前元素加入
            queue.append(i)

            # 剔除掉不在窗口中的最大值们,这里每次循环移动一格，用if即可。
            if queue[0] <= i - k:
                queue.popleft()

            # 从第一个完整窗口记录答案 
            if i >= k-1: 
                ans.append(nums[queue[0]])

        return ans 