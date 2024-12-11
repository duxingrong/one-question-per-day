"""

求根节点到叶节点数字之和

给你一个二叉树的根节点root,树中每个节点都存放一个0到9之间的数字

每条从根节点到叶节点的路径都代表一个数字

 1 
/ \
2  3 

输出:   12+13 = 25

"""


from typing import List

class TreeNode():
    def __init__(self,val=0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def sumNumbers(self,root:TreeNode):
        self.res = 0
        path = []
        
        def dfs(node,path):
            # 搜索到空节点，直接返回
            if not node:
                return 
            path.append(node)
            #遇到叶子节点，就收获结果
            if not node.left and not node.right :
                self.res+=get_sum(path) 
            #如果不是，就继续深搜
            if node.left:
                dfs(node.left,path)

            if node.right:
                dfs(node.right,path)
            #回溯
            path.pop()

       
        def get_sum(path:List[TreeNode]):
            result = ""
            for i in  range(len(path)):
                result+=str(path[i].val)

            return int(result)

        #开始深搜索
        dfs(root,path)

        return self.res

            
if __name__=="__main__":
    # 构建测试用例
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    solution = Solution()
    print(solution.sumNumbers(root))  # 输出 25

