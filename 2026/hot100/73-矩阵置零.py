"""
73. 矩阵置零

给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法

"""

"""
用矩阵自己的第一行和第一列，来当"标记数组"
第一行和第一列既是数据区，又是标记区，所以必须先用 flag 记录它们原来的状态，然后内部区域从 1 开始处理，最后再处理第一行和第一列
"""

from typing import List 

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])

        # 首先判断第一列需不需要置零
        first_col_flag = False

        for i in range(m):
            if matrix[i][0] == 0 : 
                first_col_flag = True
                break

        first_raw_flag = False
        # 判断第一行是否需要置零
        for j in range(n):
            if matrix[0][j] == 0: 
                first_raw_flag = True
                break 

        # 用第一行和第一列来做标记
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[0][j] =0
                    matrix[i][0] =0 

        # 根据标记置零
        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        
        # 根据flag置零第一行或者第一列
        if first_raw_flag:
            for j in range(n):
                matrix[0][j]=0
        if first_col_flag:
            for i in range(m):
                matrix[i][0]=0
        


