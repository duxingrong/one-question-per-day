"""
二叉树的迭代遍历
"""
from typing import List

class TreeNode():
    def __init__(self,val:int,left:None,right=None):
        self.val=val
        self.left=left
        self.right=right

#------前序遍历----根左右-----#
class Solution:
    def preorderTraversal(self,root:TreeNode)->List[int]:
#-----首先看是否根节点为空----#
        if  not root  :
            return []
        stack=[root]
        result=[]
        """
        这个循环的逻辑是，每次都会先传出根节点，然后将他的左右节点传进去
        """
        while stack:
            node=stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result



#--------后序遍历------左右根---------前序根左右，也可以做到根右左，然后反转，就是左右根！！！！-----#
class Solution:
    def postorderTraversal(self,root:TreeNode)->List[int]:
        if  not root :
            return []
        result=[]
        stack=[root]
        while stack:
            node=stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]



#------中序遍历，就是说是左根右------------#--因为访问和要执行的不是一个节点，所以要加入指针-------#
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []  # 不能提前将root结点加入stack中
        result = []
        cur = root#----借助了指针-----#
        while cur or stack:
            # 先迭代访问最底层的左子树结点
            if cur:     
                stack.append(cur)
                cur = cur.left		
            # 到达最左结点后处理栈顶结点    
            else:		
                cur = stack.pop()
                result.append(cur.val)
                # 取栈顶元素右结点
                cur = cur.right	
        return result
        
        

            
