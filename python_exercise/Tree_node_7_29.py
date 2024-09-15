"""
二叉树的层次遍历
"""
from typing import List ,Optional
from collections import deque

class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
"""
长度法,说白了就是利用首先要记录每一层的长度,就是len(queue),这样我就是知道要弹出多少个元素(也就是for循环的次数)
然后每次while循环前都会初始化一个数组level用来记录每一层的元素,最后返回一个二维数组
"""
class Solution():
    def leverOrder(self,root:Optional[TreeNode])->List[List[int]]:
        if not root:
            return []
        res=[]
        queue=deque([root]) # 初始化队列
        while deque:
            level=[] #用来记录每一层的元素的子数组
            for _ in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res

"""
递归法,
递归的参数:根节点和层数
递归的输出:二维数组
递归的终止条件: 当访问节点为时,跳到上一级
递归的单层逻辑,首先确保存在能容纳当前元素的子数组,然后将当前访问节点添加到对应的节点里面
"""

class Solution2():
    def leverOrder(self,root:Optional[TreeNode])->List[List[int]]:
        if not root:
            return []
        # 初始化多维数组用来存储结果
        levels=[]
        def traverse(node,level):
            # 终止条件:
            if not node:
                return 
            """
             确保有当前层的容器,root要放在第一个子数组里,这个代码就是用来创建第n个子数组的                                          
            """
            if len(levels)==level: 
                levels.append([])
            levels[level].append(node.val)
            traverse(node.left,level+1)
            traverse(node.right,level+1)
        # 函数实例
        traverse(root,0)
        return levels


