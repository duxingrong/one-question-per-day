"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。
"""
class TreeNode():
    def  __init__(self,val:int,left:None,right:None):
        self.val=val
        self.left=left
        self.right=right

class Solution():
    
    def maxDepth(self,root:TreeNode)->int:
        #special case
        if not root:
            return 0
        #Determine the termination condition
        if not root.left and root.right:
            return 1
        #Recursively find the depth of left and right subtrees
        left_depth=self.maxDepth(root.left)
        right_depth=self.maxDepth(root.right)
        return max(left_depth,right_depth)+1



