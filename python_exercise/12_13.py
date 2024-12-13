"""
相同的树

给定两个二叉树，编写一个函数来检验它们是否相同

如果两个树在结构上相同，并且节点具有相同的值，则认为他们是相同的

求二叉树是否对称和求二叉树是否相同几乎一致

"""
from typing import Optional

class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val = val 
        self.left = left
        self.right = right


class Solution():

    def isSameTree(self,root1:Optional[TreeNode],root2:Optional[TreeNode])->bool:
        #首先判断当前的节点
        if root1==None and root2==None :
            return True
        elif root1==None or root2==None:
            return False
        elif root1.val != root2.val:
            return False
        
        #然后递归判断左右孩子
        left = self.isSameTree(root1.left,root2.left)
        right = self.isSameTree(root1.right,root2.right)
        return left and right


"""
迭代法
"""
from collections import deque

class Solution():

    def isSameTree(self,root1:Optional[TreeNode],root2:Optional[TreeNode])->bool:
        #特殊情况
        if not root1 and not root2: return True
        if not root2 or not  root1: return False
        que = deque()
        que.append(root1)
        que.append(root2)
        while que:
            left = que.popleft()
            right = que.popleft()
            if left is None and right is None: continue
            if left is None or right is None or left.val != right.val: return False
            que.append(left.left)
            que.append(right.left)
            que.append(left.right)
            que.append(right.right)
        return True


        

if __name__=="__main__":
    # 假设已经定义了 TreeNode 类
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(1, TreeNode(2), TreeNode(3))

    sol = Solution1()
    print(sol.isSameTree(root1, root2))  # 输出 True

