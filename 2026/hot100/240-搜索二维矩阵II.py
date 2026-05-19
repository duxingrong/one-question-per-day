"""
240. 搜索二维矩阵 II

编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列

"""

"""
看到二维矩阵满足: 
每行递增
每列递增

搜索某个数，优先想到：
从右上角或者左下角开始

右上角：大了往左，小了往下

利用矩阵的有序性，每次排除一行或一列
"""


from typing import List 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        # 右上角开始
        i = 0
        j = n-1 

        while i<m and j >=0:

            if matrix[i][j] == target:
                return True 
            elif matrix[i][j]< target:
                i+=1 
            else:
                j -=1 
        
        return False 