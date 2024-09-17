"""
计算给定二叉树的所有左叶子之和。
"""
from typing import Optional
from collections import deque
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        
"""
迭代法:(层序遍历还是容易)
"""

class Solution1():
    def leftsum(self,root:Optional[TreeNode])->int:
        if not root:
            return 0
        result = 0
        queue=deque([root])
        while queue:
            node = queue.popleft()
            if node.left and node.left.left==None and node.left.right==None:
                result+=node.left.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
"""
递归法,应该算是前序(中左右)
终止条件,遇到叶子节点就返回
单层逻辑,我们处理就是对于当前节点,如果他有node.left:那么就把值加给result,然后就去向下递归遍历左右节点
"""


class Solution2():
    def __init__(self):
        self.result=0

    def leftsum(self,root:Optional[TreeNode]):
        if not root:
            return 0
        self.getsum(root)
        return self.result
        
    def getsum(self,node):
        # 终止条件
        if node.left ==None and node.right==None:
            return 
        # 单层逻辑
        if node.left and node.left.left==None and node.left.right==None:
            self.result+=node.left.val
        if node.left:
            self.getsum(node.left)
        if node.right:
            self.getsum(node.right)
   
    
        
# 创建测试二叉树
# 例如，构建如下树：
#       1
#      / \
#     2   3
#   /   
#  2    
# /
#5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left=TreeNode(2)
root.left.left.left=TreeNode(5)

# 计算并打印最小深度
solution = Solution2()
print( f"这个树的左叶子之和是{ solution.leftsum(root) }")        
 


