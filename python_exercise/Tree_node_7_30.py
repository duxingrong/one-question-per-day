"""
翻转二叉树
"""
#-----递归法---------#
class TreeNode():
    def __init__(self,val:int,left:None,right:None):
        self,val=val
        self.left=left
        self.right=right
class Solution():
    def reverseTree(self,root:TreeNode)->TreeNode:
        if not root:
            return None
        #从上到下一次遍历交换#
        root.right,root.left=root.left,root.right
        self.reverseTree(root.left)
        self.reverseTree(root.right)
        return root


