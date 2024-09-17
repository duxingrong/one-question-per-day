"""
相同的树,那就是看每个位置的元素是不是一样的,直接层序遍历出二维数组最简单
"""
from typing import Optional
from collections import deque
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

"""
迭代法,最简单(但是需要额外的两个数组来存储,空间度太高)
"""

class Solution1():
    def isSame(self,root1:TreeNode,root2:TreeNode)->bool:
        res1=self.getres(root1)
        res2=self.getres(root2)
        if res1 == res2 :
            return True
        return False
    def getres(self,node):
        if not node:
            return []
        res=[]
        queue=deque([node])
        while queue:
            node=queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
            
        
"""
递归法,想一下是怎样的(前序)
参数:两个头节点 返回:bool
终止条件,如果是空节点,return 或者当判断不相等时直接强制返回-1,
单层逻辑

"""
class Solution2():
    def isSame(self,root1:TreeNode,root2:TreeNode)->bool:
        return self.compare(root1,root2)
      
    def compare(self,node1,node2):
        #首先排除空节点:
        if node1==None and node2!=None:
            return False
        elif node1!=None and node2==None:
            return False
        elif not node1 and not node2:
            return True
        # 在排除不相等
        elif node1.val != node2.val:
            return False
        # 此时都没有返回,说明这一层通过,那就递归去判断下一层
        left=self.compare(node1.left,node2.left)
        right=self.compare(node1.right,node2.right)
        answer = left and right
        return answer
        

