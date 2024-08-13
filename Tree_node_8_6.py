"""
相同的树
"""
class TreeNode():
    def __init__(self,val:int,left:None,right:None):
        self.val=val
        self.left=left
        self.right=right
        
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.compare(p, q)
        
    def compare(self, tree1, tree2):
        if not tree1 and tree2:
            return False
        elif tree1 and not tree2:
            return False
        elif not tree1 and not tree2:
            return True
        elif tree1.val != tree2.val: #注意这里我没有使用else
            return False
        
        #此时就是：左右节点都不为空，且数值相同的情况
        #此时才做递归，做下一层的判断
        compareLeft = self.compare(tree1.left, tree2.left) #左子树：左、 右子树：左
        compareRight = self.compare(tree1.right, tree2.right) #左子树：右、 右子树：右
        isSame = compareLeft and compareRight #左子树：中、 右子树：中（逻辑处理）
        return isSame

"""
二叉的所有路径
"""
from typing import List
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        path = []
        if not root:
            return result
        self.traversal(root, path, result)
        return result
        
    def traversal(self, cur, path, result):
        path.append(cur.val)
        #这才到了叶子节点
        if not cur.left and not cur.right:
            sPath = ""
            for i in range(len(path)-1):
                sPath += str(path[i])
                sPath += "->"
            sPath += str(path[len(path)-1])
            result.append(sPath)
            return
        if cur.left:
            self.traversal(cur.left, path, result)
            path.pop() #回溯
        if cur.right:
            self.traversal(cur.right, path, result)
            path.pop() #回溯