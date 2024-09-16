"""
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明: 叶子节点是指没有子节点的节点。
与最大深度的区别在于,单层的逻辑处理需要分情况,对于一边是空,一边不是空的情况需要取不为空的一侧
"""

from typing import Optional
from collections import deque
# 二叉树的定义
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

"""
递归法(后序)
参数:头节点
返回:int
终止条件:空节点返回0
单层逻辑,得到左右深度,如果一边为空,一边不为空,则取不为空的,否则就直接取最小值
"""
class Solution1():
    def getheight(self,root:Optional[TreeNode])->int:
        # 终止条件
        if not root:
            return 0
        # 逻辑处理
        leftheight=self.getheight(root.left)
        rightheight=self.getheight(root.right)
        # 分类讨论
        if leftheight and  not rightheight:
            height= 1+leftheight
        elif rightheight and  not leftheight:
            height= 1+rightheight
        else:
            height=1+min(leftheight,rightheight)

        return height
"""
递归法(前序)
参数:头节点
返回:int
终止条件,对于空节点,直接返回
单层逻辑: 每次找到叶子节点,需要更新result的值,让他永远保持最小
"""
class Solution2():
    def __init__(self):
        self.result=float('inf') # 无穷大
    def getdepth(self,node,depth):
        # 终止条件
        if not node:
            return 
        # 单层逻辑
        if node.left==None and node.right==None:
            self.result=min(self.result , depth)
        #递归调用
        self.getdepth(node.left,depth+1)
        self.getdepth(node.right,depth+1)

    def mindepth(self,root):
        if not root  :
            return 0
        self.getdepth(root,1)
        return self.result

"""
迭代法(层序遍历)
就是记住一定是处理叶子节点,从上到下第一次找到的叶子节点的深度就是最小深度
"""
class Solution3():
    def getdepth(self,root:Optional[TreeNode])->int:
        if not root:
            return 0
        queue=deque([root])
        depth=0
        while queue:
            depth+=1
            for _ in range(len(queue)):
                node = queue.popleft()
                # 处理逻辑
                if node.left==None and node.right==None:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth




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
print("Minimum depth of the tree:", solution.getdepth(root)) 
