"""
翻转二叉树
"""
from typing import Optional  ,List
from collections import deque
# 二叉树的定义
class TreeNode():
    def __init__(self,val=0,right=None,left=None):
        self.val=val
        self.left=left
        self.right=right

"""
递归法三种都可以,但是要特别注意中序遍历,因为当我们返回到根节点后,我们的左右孩子是已经交换了,所以要继续处理统一侧孩子才对
参数:头节点,返回头节点
终止条件: 访问节点为空,返回None
一个的逻辑,left,right=right,left
"""

# 递归法--前序遍历
class Solution1():
    def inverseTree(self,root:Optional[TreeNode])->TreeNode:
        if not root:
            return None
        #逻辑(中左右)
        self.left,self.right=self.right,self.left #中
        self.inverseTree(root.left) #左
        self.inverseTree(root.right) #右        

        return root

# 递归法--后序遍历
class Solution2():
    def inverseTree(self,root:Optional[TreeNode])->TreeNode:
        #终止条件
        if not root :
            return None
        # ( 左右中 )
        self.inverseTree(root.left)
        self.inverseTree(root.right)
        self.left,self.right=self.right,self.left

        return root
        
# 递归法--中序遍历
class Solution3():
    def inverseTree(self,root:Optional[TreeNode])->TreeNode:
        if not root:
            return None
        """
        这里要左中左才对,因为以前的右反转到了左边,要继续处理左边
        """
        self.inverseTree(root.left)
        self.left,self.right=self.right,self.left
        self.inverseTree(root.left)

        return root

"""
迭代法(用栈)前序,中序,后序
""" 
# 迭代法--前序
class Solution4():
    def inverseTree(self,root:Optional[TreeNode])->TreeNode:
        if not root:
            return None
        stack=[root]
        while stack:
            node=stack.pop()
            node.left,node.right=node.right,node.left
            """
            本来是右边先进栈,但是由于首先就处理了中节点,导致左右互换,所以要先左节点(以前的右节点入栈)
            """
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root


# 迭代法--后序遍历
class Solution5():
    def inverseTree(self,root:Optional[TreeNode])->TreeNode:
        if not root:
            return None
        """
        左右中->那就左右中即可
        """
        stack=[root]
        while stack:
            node=stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left,node.right=node.right,node.left
        return root

# 迭代法--中序遍历
class Solution6():
    def inverseTree(self,root:Optional[TreeNode])->TreeNode:
        if not root:
            return None
        stack=[root]
        while stack:
            node=stack.pop()
            """
            左中右,由于你在中时候就互换了,所以要继续添加同一侧的入栈
            """
            if node.right:
                stack.append(node.right)
            self.left,self.right=self.right,self.left
            if node.right:
                stack.append(node.right)
        return root
            

# 层序遍历(迭代法)
class Solution7():
    def inverseTree(self,root:Optional[TreeNode])->TreeNode:
        if not root:
            return None
        queue=deque( [root] )
        while queue:
            for i in range(len(queue)):
                node=queue.popleft()
                node.left,node.right=node.right,node.left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
                
        

