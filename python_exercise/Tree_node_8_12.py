"""
给定两个二叉树,想象当你将它们中的一个覆盖到另一个上时,两个二叉树的一些节点便会重叠.
你需要将他们合并为一个新的二叉树.合并的规则是如果两个节点重叠,
那么将他们的值相加作为节点合并后的新值,否则不为 NULL 的节点将直接作为新二叉树的节点.
"""
from typing import Optional
from collections import deque
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

"""
用递归前序
参数:两个头节点
返回:一个新的头节点
跳出递归的条件:
每一层,我们遍历左孩子和右孩子,如果1的节点为空,就返回当前位置的2的值,2为空就返回1的,
如果都有值,那就返回加法
然后递归的去构造下一层
"""


class Solution1():
    def makeTree(self,root1:Optional[TreeNode],root2:Optional[TreeNode])->Optional[TreeNode]:
        # 终止条件
        if root1 ==None:
            return root2
        if root2 ==None:
            return root1
        # 如果都有:
        root = TreeNode()
        root.val = root1.val+root2.val

        # 递归构造下一层
        root.left = self.makeTree(root1.left,root2.left)
        root.right = self.makeTree(root2.right,root2.right)

        return root
        
        

"""
迭代法,对于两个树的操作,那就队列的元素是一个数组
思路都是一样的
"""

class Solution2():
    def makeTree(self,root1:Optional[TreeNode],root2:Optional[TreeNode])->Optional[TreeNode]:
        # 基础判断:
        if not root1:
            return root2
        if not root2:
            return root1
        queue=deque()
        queue.append((root1,root2))
        while queue:
            node1 ,node2 = queue.popleft()
            node1.val +=node2.val
            """
            巧妙,这里只需要考虑node1(因为我们新的树就是node1),如果两个都有,就需要在和并,如果1没有,那直接把2给拿过来
            """
            if node1.left and node2.left:
                queue.append((root1.left,root2.left))
            elif not node1.left:
                node1.left = node2.left

            if node1.right and node2.right:
                queue.append((root1.right,root2.right))
            elif not node1.right:
                node1.right = node2.right

        return root1 














