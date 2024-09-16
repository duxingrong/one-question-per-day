"""
给定一个二叉树，找出其最大深度。
深度:是指二叉树每个节点到叶子节点的距离,根节点本身的深度为1
高度:是指二叉树每个节点到根节点的距离,叶子节点自己的高度是1
一般求深度使用前序中左右,高度使用后序左右中,(这样才能知道上一层是多少,然后下一层在此基础上+1)
二叉树的最大深度也就是二叉树的最大高度,所以用后序求最大深度没有问题
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
递归法后序求最大深度
参数,头节点
返回,int
终止条件,当遍历到空节点时,他的高度是0,返回0
单层的逻辑:
是后序,那就先左孩子,再右孩子,然后取最大值加1,就是本层高度
"""

class Solution1():
    def getHeight(self,root:Optional[TreeNode])->int:
        # 终止条件
        if not root:
            return 0
        # 处理逻辑
        leftheight=self.getHeight(root.left)
        rightheight=self.getHeight(root.right)
        height=1+max(leftheight,rightheight)
        return height




"""
迭代法-前序,就是每一次while循环时,他会遍历一层,那就只需要每次循环depth+1即可(这就是真的是深度,而不是利用高度等于深度)
"""

class Solution2():
    def getHeight(self,root:Optional[TreeNode])->int:
        if not root:
            return 0
        queue=deque([root])
        # 初始化深度
        depth=0
        while queue:
            depth+=1
            for _ in range(len(queue)):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth



















