# 前序遍历-递归----可以理解为根左右----#


from typing import List
# 二叉树节点的定义
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#preorder---前序----traversal-----遍历-----#
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:  # 定义前序遍历方法，root为二叉树的根节点
        res = []  # 用于存储遍历结果的列表
        
        def dfs(node):  # 定义深度优先搜索函数
            if node is None:  # 如果节点为空，返回
                return
            
            res.append(node.val)  # 访问节点，将节点值加入结果列表
            dfs(node.left)  # 递归遍历左子树
            dfs(node.right)  # 递归遍历右子树
        
        dfs(root)  # 从根节点开始进行深度优先搜索
        return res  # 返回遍历结果列表




# 中序遍历-递归----#-----左根右------#
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def dfs(node):
            if node is None:    #---- 这里的 return 是结束当前函数执行，并返回到上一个调用点----#
                return
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res
    


#------后续遍历-----左右根------#
class Solution():
    def postorderTraversal(self,root:TreeNode)->List[int]:
        res=[]
        #----递归函数-----#
        def dfs(self,node):
            if node is None:
                return 
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res