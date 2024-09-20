"""
二叉树的最近公共祖先,也就是两个节点的最近的公共上位节点(可以是自己)
"""

from typing import Optional
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val = val 
        self.left = left
        self.right = right

"""
思路:我们肯定是需要找到p,q然后将他们的祖先一步一步向上返回,才能得到这个值,那么利用后序遍历和回溯就可以做到从下往上遍历
参数: 根节点,p,q
返回值:一个节点
终止条件:
1.当我们遍历到空时,那说明一直没找到,就返回当前的空节点(也就是None)
2.如果遍历的节点是p或者q,那就返回当前的节点
单层逻辑:
left = 接住上一层的返回值
right = 接住上一层的返回值
1.如果 left and right: return root
2.如果 left is None and right: return right
3.如果 left  and right is None: return left
4.return None
"""

class Solution():
    def lowestCommonAncestor(self,root:Optional[TreeNode],p:TreeNode,q:TreeNode)->Optional[TreeNode]:
        # 向下遍历的终止条件
        if not root:
            return None 
        if root == q or root ==p:
            return root
        
        # 开始遍历
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        # 递归返回的处理逻辑
        if left and right: #  说明这个节点就是要找的最近公共祖先
            return root
        elif left and right is None: 
            return left
        elif right and left is None: 
            return right
        else:
            return None









