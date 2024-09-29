"""
给定一个二叉树,我们在树的节点上安装摄像头.
节点上的每个摄像头都可以监视其父对象,自身及其直接子对象.
计算监控树的所有节点所需的最小摄像头数量.
"""

"""
和二叉树有关的东西肯定涉及到递归和回溯
输入:二叉树
返回:int
什么顺序呢?还是没有顺序?又是贪心算法,怎么贪呢?什么情况下才是一定需要添加摄像机的?

解析:
这里我们首先要想到,最好的方法就是从下往上,因为我们要保证在叶子节点的上一层放摄像头才是最好的(监控了上中下三层),所以确定是后序遍历
我们怎么知道什么时候放摄像头呢?这个就需要我们利用递归的return 一个值来记录一个节点他的左右孩子的状态(-1:未监控 0: 被监控 1:被放摄像头)
1. 左右孩子只要有一个是未监控,那该节点就要放摄像头
2. 如果左右孩子都是被监控,那该节点填入未监控,等待他的父节点放置摄像头
3. 如果左右孩子有一个被放置了摄像头,那就是该节点被监控
这里从我们的条件可以看出来,2的优先级高于3,要首先判断2,再判断3,因为哪怕你左孩子有摄像头,但是你右孩子未监控,你还是需要添加摄像头!
接下来就是一个问题? 空节点应该返回什么呢?(重点):我们的贪心是一定要在叶子节点的上一层放置摄像头:
- 如果空节点返回-1(未监控):那按照逻辑叶子节点会放入摄像头(错)
- 如果空节点返回1(有摄像头):那按照逻辑叶子节点是填入0,这样它的父节点是填入-1,而不是1(放摄像头)(错)
- 所以只能是返回0(被监控):这样叶子节点是返回-1,然后叶子节点的父节点就会是1(放入摄像头)(对)
最后一个注意点:我们从下往上遍历,会漏掉根节点需要放入摄像头的情况(需要在主函数里接受值然后判断)
"""

from typing import Optional
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val = val 
        self.left = left
        self.right = right


class Solution():
    def __init__(self):
        self.result=0
    def minCameraCover(self,root:Optional[TreeNode])->int:
        # 不要忘了根节点的处理
        if self.traversal(root)==-1:
            self.result+=1
        return self.result
    def traversal(self,node):
        # 终止条件
        if node is None:
            return 0
        left=self.traversal(node.left)
        right=self.traversal(node.right)

        # 返回时候的判断逻辑
        if left==0 and right==0: #左右孩子都被监控,也是叶子节点的情况,这时候放回未监控
            return -1
        if left==-1 or right==-1:#只要左后孩子有未监控,一定是装摄像头
            self.result+=1
            return 1
        if left==1 or right==1:# 只有左右孩子有一个有摄像头,就是被监控
            return 0
