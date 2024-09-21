"""
给出二叉搜索树的根节点,该树的节点值各不相同,清你将其转换为累加树,使每个节点的node的新值等于原树中大于或者等于node.val的值之和
"""

from typing import Optional
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val = val 
        self.left = left
        self.right = right

"""
递归法,这道题的逻辑就很明显的暗示我们需要从最大的开始处理(因为最大的他不会变),从最大的开始,就是每一个节点去加他的下一个节点的值就好了
右中左(倒序就是从大到小)
# 终止条件,如果是空,直接返回
用双指针,每一个遍历的节点去加上pre就好
"""


class Solution():
    def __init__(self):
        self.pre = 0
    def convertBST(self,root:Optional[TreeNode])->Optional[TreeNode]:
        if not root:
            return None

        def traversal(node):
            # 终止条件
            if not node:
                return 
            # 先递归找到最大的节点
            traversal(node.right)
            node.val = self.pre +node.val
            self.pre = node.val
            traversal(node.left)

        traversal(root)
        return root


"""
迭代法
"""

class Solution():
    def convertBST(self,root:Optional[TreeNode])->Optional[TreeNode]:
        if not root :
            return None
        stack = []
        cur =root
        pre = 0

        while cur or stack:
            if cur :
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur.val = pre +cur.val
                pre = cur.val
                cur =cur.left
        return root

                
                








