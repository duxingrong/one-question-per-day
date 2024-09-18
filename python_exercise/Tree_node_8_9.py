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
               

"""
递归法
参数:根节点,目标和
返回值:bool
终止条件:当遍历到叶子节点时候,如果节点的值刚好等于当前的目标值,那就是true,否则false
单层逻辑:
如果有左孩子,那就目标值-当前的val值然后去递归,然后回溯要加回来,由于我们的函数本身有返回,所以也需要继续向上返回,这样只要到叶子节点时候count成了0,说明有这个路径
"""            


class Solution2():
    def isSame(self,root:Optional[TreeNode],target:int):
        if not root:
            return False
        return self.getsum(root,target-root.val)
    def getsum(self,node,count):
        # 终止条件:
        if node.left==None and node.right==None and count==0:
            return True
        if node.left ==None and node.right==None  : 
            return False
        # 单层逻辑
        if node.left:
            count-=node.left.val
            if self.getsum(node.left,count):
                return True
            count+=node.left.val
        if node.right:
            count-=node.right.val
            if self.getsum(node.right,count):
                return True
            count+=node.right.val
        return False

"""
迭代法,不仅记录节点,还要记录累加的值
"""
class Solution3():
    def isSame(self,root:Optional[TreeNode],target:int)->bool:
        if not root :
            return False
        stack=[( root,root.val )]
        while stack:
            node,sum = stack.pop()
            # 处理逻辑
            if node.left==None and node.right==None and sum == target:
                return True
            if node.right:
                sum+=node.right.val
                stack.append( ( node.right,sum ) )
                sum-=node.right.val
            if node.left:
                sum+=node.left.val
                stack.append( ( node.left,sum ) )
                sum-=node.left.val
        return False
        
# 创建测试二叉树
# 例如，构建如下树：
#       1
#      / \
#     2   3
#   /   
#  2    
# /
#5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left=TreeNode(2)
root.left.left.left=TreeNode(5)

# 计算并打印最小深度
solution = Solution3()
print( f"{ solution.isSame(root,10) }")        
 






            
        

        
