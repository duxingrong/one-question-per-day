"""
二叉树的深度三种遍历
递归的技巧:
1.确定参数和返回值
2.确定终止条件
3.确定单层递归的逻辑
"""
from typing import List
# 二叉树的定义
class TreeNode():
    def __init__(self):
        self.val=val
        self.left=left
        self.right=right

# 前序遍历(中左右)
#这个函数需要传出来什么呢?-->输入二叉树的头节点,传出来一个数组,
class Solution():
    def preorderTraversal(self,root:TreeNode) ->List[int]: 
        # 定义一个空列表
        res=[]
        def dfs(node):
            if node is None:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res

# 中序遍历(左中右)
class Solution():
    def indexorderTraversal(self,root:TreeNode) ->List[int]:
        res=[]
        def dfs(node):
            if node is None:
                return 
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
        return res
    
# 后序遍历(左右中)
class Solution():
    def postorderTraversal(self,root:TreeNode) ->List[int]:
        res=[]
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        return res 
