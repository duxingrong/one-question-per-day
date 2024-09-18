"""
给定一个二叉树，检查它是否是镜像对称的
实质上比较的是两个树,即根节点的左右子树,所以在递归时,也需要处理两棵树
"""
from typing import Optional
from collections import deque
# 二叉树的定义
class TreeNode():
    def __init__(self,val=0,right=None,left=None):
        self.val=val
        self.right=right
        self.left=left

"""
递归法,递归的三步
参数:根节点的左右子树的头节点
返回:True or False
终止条件,比较的两对象的{
    if None : None ->true
    if 值相等:     ->true
    if 有值 : None ->False
    if None : 有值 ->False
    if 值不相等    ->False
}
单层的处理逻辑,比较左树的左孩子和右树的右孩子是否相等,左树的右孩子和右树的左孩子是否相等
"""
class Solution1():
    def isSymmetric(self,root:Optional[TreeNode])->bool:
        if not root :
            return True
        return self.compare(root.left,root.right)
        
    def compare(self,left,right):
        #终止条件
        if left==None and right!=None: return False
        if left!=None and right==None: return False
        if left.val !=right.val:      return False
        if left.val == right.val:     return True
        """
        这里只能用后序遍历(准确的说是左边左右中,右边右左中),这样才能在遍历之后得到判断是否是对称的
        """
        outside=self.compare(left.left,right.right)
        inside =self.compare(left.right,right.left)
        isSame=outside and inside #逻辑处理
        return isSame


"""
迭代法(使用队列)
相当于先比较的是左右根节点,然后传入左边的左,右边的右,左边的右,右边的左,然后弹出两个继续比较,一直重复
""" 
            
class Solution2():
    def isSymmetric(self,root:Optional[TreeNode])->bool:
        if not root: 
            return True
        queue=deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            left=queue.popleft()
            right=queue.popleft()
            if left==None and right==None:
                continue
            elif left!=None and right==None:
                return False
            elif right!=None and left==None:
                return False
            elif left.val != right.val:
                return False
            elif left.val == right.val:
                # 逻辑处理
                queue.append(left.left)
                queue.append(right.right)
                queue.append(left.right)
                queue.append(right.left)
        return True

        
"""
迭代法,使用栈
基本上和队列没有任何区别,只是比较的顺序是从最底层开始,队列是从上到下
"""
class Solution3():
    def isSymmetric(self,root:Optional[TreeNode])->bool:
        if not root:
            return True
        stack=[] # 还真得先定义,然后入栈
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            left = stack.pop()
            right=stack.pop()
            if left.val !=right.val:
                return False
            elif left==None and right!=None:
                return False
            elif right==None and left!=None:
                return False
            elif right==None and left==None:
                return True
            elif left.val == right.val:
                stack.append(left.left)
                stack.append(right.right)
                stack.append(left.right)
                stack.append(right.left)
        return True


"""
层次遍历,就是遍历所有的元素,然后反转数组,如果结果不相等,说明不是对称二叉树
"""
class Solution4():
    def isSymmetric(self,root:Optional[TreeNode])->bool:
        if not root:
            return True
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            # 确定长度,决定每次for循环中的次数
            size = len(queue)
            if size % 2 != 0:
                return False
            #初始化数组储存结果
            level_vals=[]
            for _ in range(size):
                node = queue.popleft()
                if node :
                    level_vals.append(node)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level_vals.append(None)
            if level_vals!=level_vals[::-1]:
                return False
        return True



