"""
给出一个完全二叉树，求出该树的节点个数
"""
from typing import Optional
from collections import  deque
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


"""
递归法
终止条件:遇到空节点时候,直接返回0
单层逻辑:(后序),总数等于左孩子+右孩子+1,后序遍历最简单
"""

class Solution1():
    def nodeNumber(self,root:Optional[TreeNode])->int:
        # 终止条件
        if not root:
            return 0
        # 递归调用
        leftnumber=self.nodeNumber(root.left)
        rightnumber=self.nodeNumber(root.right)
        number=1+leftnumber+rightnumber
        return number

"""
迭代法(层序遍历)
"""
class Solution2():
    def nodeNumber(self,root:Optional[TreeNode])->int:
        if not root:
            return 0
        queue= deque([root])
        number =0
        while queue:
            number+=len(queue)
            for _ in range(len(queue)):
                node =queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return number 
                
                    
"""
完全二叉树的节点求法
我们终止条件里可以添加一项,我们向最左最右遍历二叉树的深度,如果深度一样,说明是满二叉树,直接节点数量为`(2<<depth)-1`
"""

class Solution3():
    def nodeNumber(self,root:Optional[TreeNode])->int:
    # 终止条件1:
        if not root:
            return 0
    # 终止条件2:   
        leftdepth=0
        rightdepth=0
        left=root.left
        right=root.right
        while left:
            leftdepth+=1
            left=left.left
        while right:
            rightdepth+=1
            right=right.right
        if leftdepth==rightdepth:
            return (2<<leftdepth)-1 #因为2<<1 代表的是2^2,所以depth初始化为0
    # 单层逻辑
        leftnumber=self.nodeNumber(root.left)
        rightnumber=self.nodeNumber(root.right)
        return 1+leftnumber+rightnumber


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
print("Node number of the tree:", solution.nodeNumber(root))        
