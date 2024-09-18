"""
给定二叉搜索树(BST)的根节点和一个值. 你需要在BST中找到节点值等于给定值的节点. 
返回以该节点为根的子树. 如果节点不存在,则返回 NULL.
"""
from typing import Optional
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

"""
二叉搜索树的特性,所有左节点<根节点<右节点
"""

"""
迭代法最简单
"""
class Solution1():
    def search(self,root:Optional[TreeNode],target:int)->Optional[TreeNode]:
        if not root :
            return None
        # 逻辑:
        while root:
            if root.val <target:
                root = root.right
            elif root.val>target:
                root = root.left
            else:
                return root
        return None



"""
递归法
参数:目标值和头节点,返回值:节点
终止条件,如果node.val == target : return node ,如果都搜索到空节点了,还没有,返回None
单层逻辑:根据大小向不同方向递归

"""
class Solution2():
    def search(self,root:Optional[TreeNode],target:int)->Optional[TreeNode]:
        # 终止条件
        if not root:
            return None
        if root.val == target:
            return root
        # 不终止就继续递归
        elif root.val<target:
            return self.search(root.right,target)
        elif root.val>target:
            return self.search(root.left,target)

# 示例用法
# 创建一个简单的二叉搜索树
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

solution = Solution1()
target_node = solution.search(root, 4)
if target_node:
    print(f"Found node with value: {target_node.val}")
else:
    print("Node not found.")


