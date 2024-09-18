"""
找树左下角的值(我们认为最后一层最左边的值认定为是左下角的值)
肯定是叶子节点
"""
from typing import Optional
from collections import deque
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        
"""
先用迭代法层序遍历写出来,在想递归怎么写
"""
class Solution1():
    def findleftval(self,root:Optional[TreeNode])->int:
        if not root:
            return -1
        queue=deque([root])
        result = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                # 每一次记录最左边的值,然后每次都会去更新最左边的值
                if  i ==0:
                    result = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

"""
递归法,没有顺序,因为我们是在终止条件的地方进行了处理,然后只要保证每次是先遍历的左孩子,就是左下角的值
"""
class Solution2():
    def __init__(self):
        self.maxdepth=0
        self.result=0
    def findleftval(self,root:Optional[TreeNode])->int:
        if not root:
            return -1
        return self.getval(root,1)
    
    def getval(self,node,depth):
        # 判断条件-->递归顺序保证了到达新的深度时候,每次一定是先记录同一个深度的最左边的值,所以我们直接用深度当判断条件即可
        if depth>self.maxdepth:
            self.maxdepth=depth
            self.result=node.val
        if node.left:
            depth+=1
            self.getval(node.left,depth)
            depth-=1 # 体现出了回溯
        # if node.left:
        #     self.getval(node.left,depth+1) # 隐藏了回溯
        if node.right:
            depth+=1
            self.getval(node.right,depth)
            depth-=1
        return self.result

        
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
print( f"这个树的左下角值是{ solution.findleftval(root) }")        
 



