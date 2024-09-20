"""
给定二叉搜索树的根节点和要插入树的值,将值插入二叉搜索树,返回值为新的二叉搜索树的根节点，插入的值是不等于任何节点的
"""

class TreeNode():
    def __init__(self,val = 0,left = None,right = None):
        self.val = val 
        self.left = left
        self.right = right

from typing import Optional
"""
那直接秒了,因为他是不会和树上的值相等的,那么插入的值一定可以放在叶子节点
# 终止条件:
1.遇到空节点,那就说明就是这里,直接赋值: root = TreeNode(val)
# 单层逻辑
1. >节点,就递归进右子树,<节点,就递归进左子树,else: 不存在else,因为题目规定了不会相等
"""

class Solution1():
    def insertIntoBST(self,root:Optional[TreeNode],val:int)->Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        self.traversal(root,val)
        return root
    
    def traversal(self,node,val):

        if node.val > val:
            if node.left is None: # 不能少了连接的这一步
                node.left = TreeNode(val)
            else:
                self.traversal(node.left,val)
        elif node.val < val:
            if node.right is None: # 不能少了连接的这一步
                node.right = TreeNode(val)
            else:
                self.traversal(node.right,val)
    
"""
迭代法,那就更简单了,直接是按照流程来写,注意是返回根节点,所以循环里得用指针去操作,操作完后直接跳出循环
"""    
class Solution2():
    def insertIntoBST(self,root:Optional[TreeNode],val:int)->Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        cur = root 
        # 流程来
        while cur:
            if cur.val > val:
                if cur.left is None:
                    cur.left = TreeNode(val)
                    break
                else:
                    cur  =  cur.left
            elif cur.val < val:
                if cur.right is None:
                    cur.right = TreeNode(val)
                    break
                else:
                    cur = cur.right
        return root

