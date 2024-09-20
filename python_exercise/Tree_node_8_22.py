"""
将一个升序排列的有序数组,转换为一棵高度平衡的二叉搜索树(左右节点的高度绝对值不会>1)
很明显,用中序遍历才能充分利用到这个数组
找到头节点,划分左子树,右子树,然后递归构造,即可
"""
from typing import List,Optional
from collections import deque
# 二叉树的定义
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val = val 
        self.left = left
        self.right = right


"""
递归法
"""
class Solution():
    def sortedArrayToBST(self,num:List[int])->Optional[TreeNode]:
        if len(num) ==0:
            return None
        # 逻辑处理
        index = len(num)//2    #% 向上取整,//向下取整
        root_val = num[index]
        root = TreeNode(root_val)
        leftnum = num[:index]
        rightnum = num[index+1:]
        root.left =  self.sortedArrayToBST(leftnum)
        root.right = self.sortedArrayToBST(rightnum)
        return root


"""
迭代法(比递归法难太多了)
mid = left + (right - left) // 2 是求数组中间索引的最佳实践
"""

class Solution():
    def sortedArrayToBST(self,num:List[int])->Optional[TreeNode]:
        if len(num)==0:
            return None
        # 初始化
        root = TreeNode(0)
        nodeQue =  deque()
        leftQue = deque()
        rightQue = deque()

        # 给值:
        nodeQue.append(root)  # 要处理的节点
        leftQue.append(0)     # 要处理的左索引
        rightQue.append(len(num)-1) # 要处理的右索引

        while nodeQue:
            node = nodeQue.popleft()
            left = leftQue.popleft()
            right = rightQue.popleft()
            mid = left +(right-left)//2
            node.val = num[mid]
            # 构造左孩子
            if left <= mid-1:
                node.left = TreeNode(0)
                nodeQue.append(node.left)
                leftQue.append(left)
                rightQue.append(mid-1)

            if right >= mid+1:
                node.right = TreeNode(0)
                nodeQue.append(node.right)
                leftQue.append(mid+1)
                rightQue.append(right)

        return root

        












