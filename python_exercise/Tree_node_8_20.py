"""
给定一个二叉树的根节点root,和一个值key,删除二叉搜索树中key对应的节点,并且保证二叉搜索树的性质不变,返回新的根节点
"""

from typing import Optional

class TreeNode():
    def __init__(self,val = 0,left=None,right=None):
        self.val = val 
        self.left = left
        self.right=right


"""
递归法,
参数:key和根节点
返回:新的根节点

# 终止条件:
1. 如果直接遍历到空节点了,说明没找到,直接return None(特殊)
找到的时候的情况:
2. 如果是在叶子节点处找到了,那直接最好了,只需要返回None
3. 如果目标节点的左为空,右不为空,那就是由右孩子来替换目标节点的位置
4. 如果目标节点的右为空,左不为空,那就是由左孩子来替换目标节点的位置
5. 如果左右都不为空,是最难的情况,我们需要用左右孩子替换,并且,如果是用左孩子接住,那右孩子就要放到左子树的最大值下面,右孩子接住,左子树就要放到右子树的最小值下面

# 返回的处理逻辑
如果key > node.val: 那么就是node.right = 接住 递归的返回值
如果key < node.val: 那么就是node.left = 接住 递归的返回值
最后返回root(这个就是新的根节点了)
"""

class Solution():
    def deleteNode(self,root:Optional[TreeNode],key:int)->Optional[TreeNode]:
        # 终止条件
        if not root:
            return None
        if root.val == key:
            if root.left == None and root.right == None :
                return None
            elif root.left and root.right ==None:
                return root.left
            elif root.right and root.left ==None:
                return root.right
            else:
                # 选择用右孩子来替换
                cur = root.right
                while cur.left is not None:
                    cur = cur.left # 找到了右子树的最小值
                cur.left =  root.left
                return root.right
        
        # 返回的处理逻辑
        if root.val>key:
            root.left = self.deleteNode(root.left,key)
        elif root.val<key:
            root.right = self.deleteNode(root.right,key)

        return root




"""
迭代法
"""
class Solution():
    def deletetarget(self,node):
        if node.left==None and node.right ==None:
            return None
        elif node.right is None:
            return node.left
        elif node.left is None:
            return node.right
        else:
            cur = node.right
            while cur.left is not None:
                cur =cur.left
            cur.left = node.left
            return node.right

    def deleteNode(self,root:Optional[TreeNode],key:int)->Optional[TreeNode]:
        # 特殊
        if not root:
            return root
        cur = root
        pre = None
        # 就是要找到要处理的节点,以及他的父节点
        while cur:
            if cur.val == key:
                break
            pre = cur 
            if cur.val > key:
                cur = cur.left
            elif cur.val < key:
                cur = cur.right
        # 对节点的处理
        if pre is None: # 说明头节点就是目标节点
            return self.deletetarget(cur)
        # 还需要知道是父节点的哪一个孩子
        if pre.left and pre.left.val == key: # 证明是处理的左孩子
            pre.left = self.deletetarget(cur)
        elif pre.right and pre.right.val == key:
            pre.right = self.deletetarget(cur)
        return root

            


































