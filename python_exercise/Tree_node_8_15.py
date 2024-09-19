"""
给你一个所有节点为非负值的二叉搜索树,请你计算树中的任意两节点的差的绝对值的最小值
"""
from typing import Optional
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

"""
左中右,在递归法中使用双指针,每次都让pre指向遍历的上一个节点,然后看做减法,这样更加完美利用了二叉搜索树的特性
由于到空节点时候都是返回,然后退到叶子节点的时候,这时候self.pre还是None,但是终于执行了self.pre = node
"""

class Solution2():
    def __init__(self):
        self.result = float('inf')
        self.pre = None #前指针开局为空
    def minval(self,root:Optional[TreeNode])->int:
        self.getminval(root)
        return self.result
    def getminval(self,node):
        # 终止条件
        if not node:
            return
        self.getminval(node.left)
        if self.pre is not None:
            self.result = min(self.result , node.val-self.pre.val)
        self.pre = node
        self.getminval(node.right)
"""
迭代法(感觉思路不好想)
"""
class Solution3():
    def minval(self,root:Optional[TreeNode])->int:
        # 不讨论root为空
        stack=[]
        pre = None
        cur = root
        result = float('inf')
        # 处理逻辑
        """
        当cur遍历到空节点时,我们需要立刻返回到上一层,利用栈
        """
        while cur is not None or len(stack)!=0:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                cur  = stack.pop()
                if pre is not None:
                    result = min(result,cur.val-pre.val)
                pre = cur 
                cur = cur.right
        return result

    #     4
    #    / \
    #   2   6
    #  / \
    # 1   3
    #
# 构建二叉搜索树
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

# 创建解决方案对象并计算最小差值
solution = Solution3()
min_difference = solution.minval(root)

print("最小差的绝对值是:", min_difference)
