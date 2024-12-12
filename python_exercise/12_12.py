"""
将二叉搜索树变平衡

给你一棵二叉搜索数，请你返回一棵平衡后的二叉搜索树，新生成的数应该与原来的树有着相同的节点值

如果一棵二叉搜索树中，每个节点的两颗子树高度差不超过1，我们就称这颗二叉搜索树是平衡的

返回任意一种构造方法就好
"""


"""
方法很笨，就是将二叉搜索树中序遍历成数组，然后冲重新构建二叉树
"""

class TreeNode():
    def __init__(self,val=0,left = None , right = None):
        self.val = val 
        self.left = left 
        self.right = right 


class Solution():
    def balanceBST(self,root:TreeNode):
        #深搜
        def dfs(node,res):
            #终止条件
            if not node :
                return 
            #递归逻辑
            if node.left:
                dfs(node.left,res)
            res.append(node.val)
            if node.right:
                dfs(node.right,res)
                
        #将数组重新变成平衡二叉搜索树,同样是利用递归来构建，巧妙
        def numsTotree(res, left , right ):
            if right<left : 
                return None 
            mid = (left+right)//2
            root = TreeNode(res[mid])
            root.left = numsTotree(res, left, mid-1)
            root.right = numsTotree(res ,mid+1 , right)
            return root 
     
        #主函数
        res = []
        dfs(root, res)
        root = numsTotree(res, 0 , len(res)-1)
        return root 
    
        

            


