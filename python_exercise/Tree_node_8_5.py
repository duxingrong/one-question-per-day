"""
给定一个二叉树,返回所有从根节点到叶子节点的路径.
说明: 叶子节点是指没有子节点的节点.
"""
from typing import  Optional  ,List
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

"""
递归法,这里使用的是前序遍历,从终止条件就可以看出
参数:根节点
传出:是一个二维数组
终止条件:当遍历到叶子节点的时候,就直接将子数组添加到结果中
单层逻辑:因为我们就是需要在叶子节点出得道路径.那么对于非叶子节点,就递归的去找叶子节点
回溯:当我们记录一组路径后,我们为了重新开始新的路径,就需要将当前处理完的节点给pop除去,回溯到分岔口然后去记录新的路径
"""

class Solution1():
    def getpath(self,node,path,result):
        path.append(node.val) # 每次遍历,都会将path路径里加上当前指针节点的val

        # 终止条件
        if node.left==None and node.right==None:
            sPath='->'.join(map(str,path))
            result.append(sPath)
            return 
        # 逻辑,不是叶子节点,就递归去遍历
        if node.left:
            self.getpath(node.left,path,result)
            # 当跳出一级后,需要处理掉之前的节点
            path.pop()
        if node.right:
            self.getpath(node.right,path,result)
            # 当跳出一级后,需要处理掉之前的节点
            path.pop()
       
        
    def path(self,root:Optional[TreeNode]):
        result=[]
        path=[]
        if not root:
            return result
        self.getpath(root,path,result)
        return result


"""
迭代法,他的逻辑还有点看着答案写出来的
"""
class Solution2():
    def path(self,root:TreeNode)->List[str]:
        # 题目中节点数量至少为1
        stack,path_st,result=[root],[str(root.val)],[]
        while stack:
            cur = stack.pop()
            path=path_st.pop()
            # 叶子节点
            if cur.left==None and cur.right==None:
                result.append(path)

            if cur.right:
                stack.append(cur.right)
                path_st.append(path+"->"+str(cur.right.val))
            if cur.left:
                stack.append(cur.left)
                path_st.append(path+"->"+str(cur.left.val))
        return result



# 创建测试二叉树
# 例如，构建如下树：
#       1
#      / \
#     2   3
#   /   
#  2    
# /
#5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left=TreeNode(2)
root.left.left.left=TreeNode(5)

# 计算并打印最小深度
solution = Solution2()
print( solution.path(root))        
       
