"""
48. 旋转图像

给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像

"""

"""
顺时针旋转90°等于先上下反转,再沿着主对角线翻转
"""

from typing import List 

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)

        # 先上下反转
        for i in range(n//2):
            matrix[i],matrix[n-1-i] = matrix[n-1-i],matrix[i]

        # 再沿着对角线反转
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        

        