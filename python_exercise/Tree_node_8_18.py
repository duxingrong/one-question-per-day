"""
二叉搜索树的公共祖先,二叉搜索树,因为二叉搜索树是顺序的,所以如果节点值大于p,q的最大值,那就说明要去左子树里继续搜,如果小于,就要去右树里继续搜索,如果节点值在区间内,那么这个节点一定是最近公共祖先,因为你接下来不管去左还是右,你都会错过p或者q
"""

from typing import  Optional

class TreeNode():
    def __init__(self,val =0,left=None,right=None):
        self.val = val 
        self.left = left
        self.right = right


"""
参数根节点,p,q 返回,一个节点
终止条件:
1.遍历到空了,直接返回空
2.如果这个节点大于,那就向左递归 , left =接住返回值, 如果你返回值有值,那就是找到了,返回left
3.如果节点小于,向右递归 , right =接住返回值, 如果你返回值有值,那就是找到了,返回right
4.return root
"""


class Solution():
    def lowestCommonAncestor(self,root:Optional[TreeNode],p:TreeNode,q:TreeNode)->Optional[TreeNode]:
        # 终止条件
        if not root:
            return None
        if root.val >p.val and root.val > q.val:
            left = self.lowestCommonAncestor(root.left,p,q)
            if left:
                return left
        elif root.val <p.val and root.val < q.val:
            right = self.lowestCommonAncestor(root.right,p,q)
            if right:
                return right
        else: 
            return root

"""
迭代法
"""
class Solution1():
    def lowestCommonAncestor(self,root:Optional[TreeNode],p:TreeNode,q:TreeNode)->Optional[TreeNode]:
        if not root:
            return None
        while root:
            if root.val > p.val and root.val>q.val:
                root = root.left
            elif root.val <p.val and root.val <q.val:
                root = root.right
            else:
                return root

            
        

        


