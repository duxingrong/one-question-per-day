"""
构造二叉树
根据一棵树的中序遍历和后序遍历来构造二叉树(给你二个数组,还原二叉树)
"""
from typing import List
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

"""
利用中序和后序来还原一棵二叉树
由后序找到头节点,然后带入中序区分左中序和右中序,还后根据数量可以找到左后序和右后序,然后左中序,左后序还原左子树,右中序,右后序还原右子树.
"""
class Solution1():
    def makeTree(self,num1:List[int],num2:List[int])->TreeNode:
        # 基础条件：如果中序或后序数组为空，返回None
        if not num1 or not num2:
            return None
        """
        1.找到根节点
        2.切割中序数组和后序数组
        3.遇到叶子节点时,加他返回
        """
        # 切割中序数组:
        root_val = num2[-1]
        root=TreeNode(root_val)
        root_index=num1.index(root_val)
        leftnum1=num1[:root_index]
        rightnum1=num1[root_index+1:]
        # 切割后序数组
        leftnum2=num2[:len(leftnum1)]
        rightnum2=num2[len(rightnum1):-1]
        root.left=self.makeTree(leftnum1,leftnum2)
        root.right=self.makeTree(rightnum1,rightnum2)
        return root
"""
前序加中序(逻辑是一样的)
"""
class Solution2():
    def makeTree(self,preorder:List[int],inorder:List[int])->TreeNode:
        # 特殊情况处理
        if not preorder or  not inorder:
            return None
        # 分割前序和中序
        root_val=preorder[0]
        root=TreeNode(root_val)
        #开始分割
        root_index=inorder.index(root_val)
        # 中序列(左中右)
        leftinorder=inorder[:root_index]
        rightinorder=inorder[root_index+1:]
        # 前序列(中左右)
        leftpreorder=preorder[1:len(leftinorder)+1]
        rightpreorder=preorder[len(leftinorder)+1:]
        # 递归
        root.left =self.makeTree(leftpreorder,leftinorder)
        root.right=self.makeTree(rightpreorder,rightinorder)
        return root


        
       
num1=[3,4,2,5,1]# 中
num2=[3,2,4,1,5]# 后
num3=[5,4,3,2,1]# 前

solution=Solution2()
print(f"头节点的值是{solution.makeTree(num3,num1).val}")






