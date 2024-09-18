"""
给定一个二叉树,验证其是否是一个有效的二叉搜索树
二叉搜索树的定义:所有的左节点小于根节点小于右节点
"""

from typing import Optional
from collections import deque

class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

"""
递归法,那也肯定是后序,一层一层判断是不是,向上返回,有不满足的False否则return True
"""

class Solution1():
    def isValidBST(self,root:Optional[TreeNode])->bool:
        # 终止条件
        if not root:
            return True
        if root.left and root.left.val >=root.val:
            return False
        if root.right and root.right.val <=root.val:
            return False
        # 单层处理
        left= self.isValidBST(root.left)
        right= self.isValidBST(root.right)
        return left and right


"""
迭代法,那就不用说了,按步骤即可
"""
class Solution2():
    def isValidBST(self,root:Optional[TreeNode])->bool:
        if not root:
            return True             #  一般一个节点也认为是有效的二叉搜索树
       # 一层一层判断就好 
        queue=deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.left and node.left.val >=node.val:
                return False
            if node.right and node.right.val <=node.val:
                return False
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return True








