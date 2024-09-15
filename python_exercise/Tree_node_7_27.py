"""
二叉树的迭代遍历
"""

from typing import List

# 二叉树的定义
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

# 二叉树的前序遍历
class Solution1():
    def preorderTraversal(self, root: TreeNode)-> List[int]:
    # 遍历的节点和处理的节点是同一个?
        if not root :
            return []
        stack=[root] #用来存放处理节点
        res=[] #用来存放结果
        while stack:
            node = stack.pop()
            # 中节点先处理
            res.append(node.val)
            # 右孩子先进栈
            if node.right:
                stack.append(node.right)
            # 左孩子先进栈
            if node.left:
                stack.append(node.left)
        return res

# 二叉树的后序遍历
"""
由前序是中左右,而后序是左右中,所以改变顺序然后反转数组即可!(因为处理节点和遍历节点是同一个)
"""

class Solution2():
    def postorderTraversal(self,root:TreeNode)->List[int]:
        if not root:
            return []
        stack=[root]
        res=[]
        while stack:
            node=stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        res=res[::-1]
        return res


"""
中序遍历由于访问节点和处理节点不是同一个,所以是不同的逻辑处理
先一路向左,访问的节点全部入栈,如果为空,就从栈中取出元素进行处理,然后看是否有右孩子,如果有,加入栈,然后继续循环
"""
class Solution3():
    def indexorderTravesal(self,root:TreeNode)->List[int]:
        if not root:
            retun []
        res=[]
        stack=[]
        cur=root
        while stack or cur:
            # 先访问最深层的左子树节点:
            if cur:
                stack.append(cur)
                cur=cur.left
            # 为空则弹出节点进行处理:
            else:
                cur = stack.pop()
                res.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                cur = cur.right
        return res
            




            

