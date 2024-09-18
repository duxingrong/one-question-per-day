"""
给定一个不含重复元素的整数数组.一个以此数组构建的最大二叉树定义如下：
二叉树的根是数组中的最大元素。
左子树是通过数组中最大值左边部分构造出的最大二叉树。
右子树是通过数组中最大值右边部分构造出的最大二叉树。
通过给定的数组构建最大二叉树，并且输出这个树的根节点。
"""
from typing import List, Optional
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

"""
和给两个数组是一个道理:
1.找到最大值,然后值赋给root.val.由max_index分割左数组和右数组,然后递归去构造下一层
"""

class Solution1():
    def makeTree(self,num:List[int])->Optional[TreeNode]:
        # 终止条件
        if not num:
            return None
        # 创建第一层根节点
        root_val=max(num)
        root=TreeNode(root_val)
        max_index = num.index(root_val)

        # 分割数组去构造下一层
        leftnum = num[:max_index]
        rightnum = num[max_index+1:]
        # 递归构造第二层
        root.left = self.makeTree(leftnum)
        root.right = self.makeTree(rightnum)
        return root


num = [5,4,8,2,3]

solution=Solution1()
root = solution.makeTree(num)
# 打印节点值
print(root.val)
print(root.left.val if root.left else None)
print(root.right.val if root.right else None)
print(root.left.right.val if root.left and root.left.right else None)
print(root.left.left.val if root.left and root.left.left else None)
print(root.right.left.val if root.right and root.right.left else None)
print(root.right.right.val if root.right and root.right.right else None)





