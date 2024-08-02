"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。
"""
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution():
    def minDepth(self,root:TreeNode)->int:
        #---two method for return---#
        if not root:
            return 0
        if not root.left and not root.right:
            return 1           
        left_depth=self.minDepth(root.left)   if root.left  else float('inf')
        right_depth=self.minDepth(root.right) if root.right  else float('inf')
        return min(left_depth,right_depth)+1

       
# 创建测试二叉树
# 例如，构建如下树：
#       1
#      / \
#     2   3
#        /
#       4
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)

# 计算并打印最小深度
solution = Solution()
print("Minimum depth of the tree:", solution.minDepth(root)) 