"""

二叉树的最大路径和

二叉树的路径被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中至多出现一次。该路径至少包含一个节点，且不一定经过根节点。

路径和是路径中各节点值的总和

给你一个二叉树的根节点root,返回其最大路径和

"""

# 这里需要注意的是，题目说了不一定过根节点，说明不是从根节点出发的最大路径和,而是从任意节点出发的最大路径和

"""
递归+后序遍历+动态规划
- 递归地计算每个节点的左右子树的最大贡献值(也就是从该节点出发能够得到的最大路径和)
- 以某个节点为根的路径的最大和，可能有以下几种情况:
    。仅包含该节点
    。该节点加上左子树路径的最大和
    。该节点加上右子树路径的最大和
    。该节点加上左右子树路径的最大和(此时路径从左子树穿过当前节点到右子树)
- 如果子树路径的和为负数，不如不选择该路径。贡献值必须是max(0,子树路径和)
- 每次在递归过程中，尝试更新全局的maxSum,它记录当前遍历过的最大路径和.
"""


class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
class Solution:
    def maxPathSum(self,root:Optional[TreeNode])->int:

        self.maxSum = float('-inf') # 初始化设置为负无穷

        def maxGain(node:Optional[TreeNode])->int:
            if not node:
                return 0

            # 递归计算左右子树的最大贡献值
            leftGain = max(maxGain(node.left),0)
            rightGain = max(maxGain(node.right),0)

            # 计算当前节点的最大路径和
            currentMaxPath = node.val +leftGain+rightGain

            # 更新全局的maxSum
            self.maxSum = max(self.maxSum ,currentMaxPath)

            # 返回一条最优路径给父节点(只能选择一条路径)
            return node.val +max(leftGain ,rightGain)

        maxGain(root) #出发递归

        return self.maxSum  # 这里一定会更新为整数
















