"""
给定一个二叉树和一个目标和,判断该树中是否存在根节点到叶子节点的路径,这条路径上所有节点值相加等于目标和.
"""
from typing import Optional
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

"""
迭代法是无敌的,层序遍历
"""

class Solution1():
    def __init__(self):
        self.results=[]

    def isSame(self,root:Optional[TreeNode],target:int)->bool:
        if not root:
            if target==0:
                return True
            return False
        self.getsum(root)
        for result  in self.results:
            if result == target:
                return True
        return False
            
    def getsum(self,node):
        stack=[node]
        sum = 0
        while stack:
            node=stack.pop()
            # 处理做了记号的
            if node==None:
                node=stack.pop()
                sum-=node.val
            sum +=node.val
            stack.append(node)
            stack.append(None)
            if node.left ==None and node.right==None:
                self.results.append(sum)
                sum-=node.val
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
               

            
            
            
        

        
