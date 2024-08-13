"""
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，
那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
"""
class TreeNode():
    def __init__(self,val:int,left:None,right:None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # 递归终止条件: 
        #  但凡有一个节点为空, 就立刻返回另外一个. 如果另外一个也为None就直接返回None. 
        if not root1: 
            return root2
        if not root2: 
            return root1
        # 上面的递归终止条件保证了代码执行到这里root1, root2都非空. 
        root1.val += root2.val # 中
        root1.left = self.mergeTrees(root1.left, root2.left) #左
        root1.right = self.mergeTrees(root1.right, root2.right) # 右
        
        return root1 # 重复使用了题目给出的节点而不是创建新节点. 节省时间, 空间. 
