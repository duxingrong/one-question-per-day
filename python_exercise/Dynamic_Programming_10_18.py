"""
房子呈现二叉树,如果两个相连的房子在同一天晚上被打劫,房屋将自动报警
"""

from typing import Optional
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val = val 
        self.left = left
        self.right = right

"""
动态数组+二叉树
和二叉树有关,那就一定有递归,可能有回溯,此时又和动态规划有关,难点也是在于dp数组的定义和含义

dp=[不偷,偷] 每一个节点都用一个dp数组来表示,dp[0]:不偷当前节点能得到的最大价值,dp[1]:偷当前节点能得到的最大价值
遍历到一个节点时: 
如果偷:那就是cur.val+left[0]+right[0] 就是当前节点的值加上左孩子不偷的最大价值和右孩子不偷的最大价值
如果不偷: 那就是max(left)+max(right) 左右孩子取最大的那个值(注意:这里不是说我不偷就一定会偷左右孩子,而是看偷与不偷谁更大)
从这个定义就能确定遍历顺序为后序遍历,因为当前的返回值要依赖左右孩子给的返回值
"""

from typing import List

class Solution():
    def rob(self,root:TreeNode)->int:
        if not root:
            return 0
        nums=self.dfs(root)
        return max(nums)

    def dfs(self,node)->List[int]:
        #空节点
        if not node :
            return [0,0] 
        
        #后序遍历
        left=self.dfs(node.left)
        right=self.dfs(node.right)

        value1=node.val+left[0]+right[0] #偷
        value2=max(left)+max(right) #不偷

        return [value2,value1]



