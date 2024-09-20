"""
修剪二叉搜索树,同时给定最小边界L和最大边界R,二叉搜索树的所有节点的值都需要在[L,R]内,返回二叉树的根节点
"""

from typing import Optional

class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


"""
递归法,终止条件: 
如果节点<=L: if node.left ==None and node.right = None: return None; if node.right: 循环找到边界值返回
如果节点>=R: if node.left ==None and node.right = None: return None; if node.left: 循环找到边界值返回
如果在区间内部, node.left = 接住递归 node.right = 接住递归 return node
"""

class Solution():
    def trimBST(self,root:Optional[TreeNode],L:int,R:int)->Optional[TreeNode]:
        # 特殊处理(也是底层处理)
        if not root :
            return None
        # 底层终止条件处理
        if root.val <L:
            if root.right is None:
                return None
            else:
                cur = root.right
                while cur is not None:
                    if cur.val >= L:
                        break
                    cur = cur.right
                return cur
        if root.val >R:
            if root.left is None:
                return None
            else:
                cur = root.left
                while cur is not None:
                    if cur.val <=R:
                        break
                    cur = cur.left
                return cur
        # 返回的逻辑
        root.left = self.trimBST(root.left,L,R)
        root.right = self.trimBST(root.right,L,R) 

        return root

"""
实际上,你在处理区间内部的时候,进行的修剪同样是可以用递归处理
"""
class Solution():
   def trimBST(self,root:Optional[TreeNode],L:int,R:int)->Optional[TreeNode]:
        if not root :
            return None
         # 底层终止条件处理
        if root.val <L:
            return self.trimBST(root.right,L,R)
        if root.val >R:
           return self.trimBST(root.left,L,R)
        # 返回的逻辑
        root.left = self.trimBST(root.left,L,R)
        root.right = self.trimBST(root.right,L,R) 

        return root

"""
迭代法(绝了)
"""
class Solution():
   def trimBST(self,root:Optional[TreeNode],L:int,R:int)->Optional[TreeNode]:
        if not root :
            return None
        # 首先保证头节点在区间内
        while root and (root.val <L or root.val >R):
            #小于向右走,大于向左走
            if root.val <L:
                root = root.right
            else:
                root = root.left

        # 保证左子树所有值>=L,这里利用两个循环,找到满足的节点后重新更新指针,继续让他的左孩子满足这个规律
        cur = root   
        while cur:
            while cur.left and cur.left.val <L:
                cur.left = cur.left.right   
            cur = cur.left
        # 接下来使得他的右孩子满足在区间内
        cur = root 
        while cur :
            while cur.right and cur.right.val >R:
                cur.right = cur.right.left
            cur = cur.right

        # 输出头节点
        return root


