"""
统一的迭代法遍历二叉树
"""
from typing import List
# 二叉树的定义
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

"""
统一的迭代法,无论前中后序,都可以用一套代码来完成
对于进入过栈的元素,再次进栈后需要进行标记(加空节点!)
"""

# 迭代法中序遍历(左中右)---->对应进栈的顺序就是右中左
class Solution2():
    def postorderTraversal(self,root:TreeNode)->List[int]:
        if not root:
            return []
        res=[]
        stack=[root]
        while stack:
            node = stack.pop()
            if node != None:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                stack.append(None) #中节点访问过 ,但是还没有处理,加入空节点做标记
                if node.left:
                    stack.append(node.left)
            else: #只有遇到空节点的时候,才将下一个节点放进结果集里
                node=stack.pop()
                res.append(node.val)
        return res

# 迭代法前序遍历(中左右)---->进栈为右左中
class Solution1():
    def preorderTravelsal(self,root:TreeNode)->List[int]:
        if not root:
            return []
        stack=[root]
        res=[]
        while stack:
            node =stack.pop()
            if node !=None:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                stack.append(node)
                stack.append(None)
            else:
                node = stack.pop()
                res.append(node.val)
        return res

# 迭代法后序遍历(左右中)---->进入栈的顺序为(中右左)
class Solution3():
    def postorderTraversal(self,root:TreeNode)->List[int]:
        if not root:
            return []
        stack=[root]
        res=[]
        while stack:
            node=stack.pop()
            if node != None:
                stack.append(node)
                stack.append(None)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            else:
                node=stack.pop() 
                res.append(node.val)
        return res

                







