"""
11. 盛最多水的容器

给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器

"""


"""
1. left 和 right 先站在最两边，宽度最大
2. 计算当前面积
3. 谁更矮，谁决定当前高度
4. 对于这个短边来说，他已经拿到了最大宽度
5. 如果继续保留它，宽度只会变小，高度又被它限制，不可能更优
6. 所以舍弃短边
7. 重复这个过程，直到所有可能成为最大值的情况都被考虑或排除
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0 
        right = len(height) -1 
        ans = 0 

        while left < right : 
            
            # 先计算当前的面积
            s = (right-left)*min(height[left],height[right])
            ans = max(ans,s)

            if height[left] <= height[right]:
                left +=1 
            else:
                right -=1 

        return ans 
