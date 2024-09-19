"""
求二叉搜索树中的众数,如果有多个,就取多个
"""
from typing import Optional,List
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left=left
        self.right=right
"""
直接中序遍历得数组,然后利用哈希表出众数
"""

class Solution0():
    def __init__(self):
        self.result = []
        self.num =[]

    def dfs(self,node):
        # 终止条件
        if not node:
            return 
        # 中序
        self.dfs(node.left)
        self.num.append(node.val)
        self.dfs(node.right)

    def getans(self):
        # 创建空字典
        stable={}
        # 遍历数组
        for val in self.num:
            stable[val] = stable.get(val,0)+1

        # 找到最大的众数
        max_count = 0
        for num ,count in stable.items():
            if count > max_count:
                max_count = count
                self.result=[num]  # 大的话直接更新
            elif count == max_count:
                self.result.append(num) # 一样就添加
    def getnum(self,root:Optional[TreeNode])->List[int]:
        self.dfs(root)
        self.getans()
        return self.result

"""
递归法,在遍历二叉搜索树的时候就可以做到找到众数
一且的处理都是在遍历的时候就做到
"""
class Solution1():
    def __init__(self):
        self.result = []
        self.pre = None
        self.max_count = 0
        self.count = 0
    
    def findmode(self,root:Optional[TreeNode]):
        # 遍历的终止条件
        if not root:
            return 
        # 左
        self.findmode(root.left)
        # 中处理
        if self.pre == None: # 他还没有值,说明此时是root到了叶子节点
            self.count =1
        elif self.pre.val == root.val:
            self.count+=1
        elif self.pre.val != root.val:
            self.count =1

        self.pre =root

        if self.count>self.max_count:
            self.max_count = self.count
            self.result=[root.val]
        elif self.count == self.max_count:
            self.result.append(root.val)
        #右
        self.findmode(root.right)

    def findMode(self,root:Optional[TreeNode])->List[int]:            
        self.result = []
        self.pre = None
        self.max_count = 0
        self.count = 0

        self.findmode(root)
        return self.result
"""
迭代法,模拟递归,也是左中右的遍历顺序
""" 

class Solution:
    def findMode(self, root):
        st = []
        cur = root
        pre = None
        maxCount = 0  # 最大频率
        count = 0  # 统计频率
        result = []

        while cur is not None or st:
            if cur is not None:  # 指针来访问节点，访问到最底层
                st.append(cur)  # 将访问的节点放进栈
                cur = cur.left  # 左
            else:
                cur = st.pop()
                if pre is None:  # 第一个节点
                    count = 1
                elif pre.val == cur.val:  # 与前一个节点数值相同
                    count += 1
                else:  # 与前一个节点数值不同
                    count = 1

                if count == maxCount:  # 如果和最大值相同，放进result中
                    result.append(cur.val)

                if count > maxCount:  # 如果计数大于最大值频率
                    maxCount = count  # 更新最大频率
                    result = [cur.val]  # 很关键的一步，不要忘记清空result，之前result里的元素都失效了

                pre = cur
                cur = cur.right  # 右

        return result
     



# Example usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)

solution = Solution0()
print(solution.getnum(root))  # Output should be [2]       
