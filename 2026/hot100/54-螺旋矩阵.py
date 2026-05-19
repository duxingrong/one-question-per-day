"""
54. 螺旋矩阵

给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素

"""

"""
就是不断地数元素

上边界
下边界
左边界
右边界

易错点：前两步会改变边界，所以后两步要确认还有没有剩余地行和列，避免重复取元素
"""

from typing import List 

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix)
        n = len(matrix[0])

        ans = [] 

        left = 0 
        right = n-1 
        top = 0 
        bottom = m -1 

        while left <=right and top <= bottom:

            # 上边界，左到右
            for j in range(left,right+1):
                ans.append(matrix[top][j])
            
            top +=1 

            # 右边界
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            
            right -=1 

            # 下边界，此时需要注意还有没有下边界
            if top <=bottom:
                for j in range(right,left-1,-1):
                    ans.append(matrix[bottom][j])

                bottom-=1
            
            # 左边界
            if left <= right:
                for i in range(bottom,top-1,-1):
                   ans.append(matrix[i][left])

                left +=1 

        return ans  
