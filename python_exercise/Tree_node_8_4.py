"""
给定一个二叉树,判断它是否是高度平衡的二叉树.

本题中,一棵高度平衡二叉树定义为:一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1.
"""
from typing import Optional
# 二叉树的定义
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

"""
递归法,很明显高度用的是后序遍历
终止条件:
当遇到空节点时,直接返回高度0给上一层
单层逻辑:
当我发现我的左右子树已经相差大于1之后,直接强制返回-1就好
得道左右子树的高度差,如果差值大于1,则返回-1,如果满足条件,则返回的是1+max(左高度,右高度)
用两个函数来完成逻辑更清晰
"""
class Solution1():
    def isBalanced(self,root:Optional[TreeNode])->bool:
        if self.getheight!=-1:
            return True
        else:
            return False
    def getheight(self,node:Optional[TreeNode])->int:
        # 终止条件
        if not node :
            return 0
        # 单层逻辑 
        leftheight=self.getheight(node.left)
        if leftheight==-1:
            return -1
         rightheight=self.getheight(node.right)
        if rightheight==-1:
            return -1
       
        if abs(leftheight-rightheight)>1:
            return -1
        else:
            return 1+max(leftheight,rightheight)


