"""
填充每个节点的下一个右侧节点指针

给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点

填充节点的next指针，让这个指针指向其下一个右侧节点，如果找不到下一个右侧节点，则将next指针设置为None

初始状态下，所有next指针都被设置为None

          1 ->None
    2  ------> 3->None 
4  ---> 5 -->6 ---> 7 ->None
"""

"""
先用迭代法理解?
"""
from typing import Optional
from collections import deque



class TreeNode():
    def __init__(self,val = 0,next=None,left=None,right=None):
        self.val =val 
        self.left = left
        self.right = right
        self.next = next


class Solution():
    def connect(self,root:Optional[TreeNode])->Optional[TreeNode]:
        #特殊情况
        if not root:
            return None

        que = deque()
        que.append(root)
        #用prev来记录前一个值，相当于for循环第一个不处理
        while que:
            prev = None
            size = len(que)#记录每一层长度，因为中途que的长度会变，不直接用len(que)

            for _ in range(size):
                cur = que.popleft()

                #赋值next
                if prev:
                    prev.next = cur
                prev = cur

                #加入队列
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)

                #最后一个不用处理，本来就是None
        return root


"""
递归法：
**关键的点在于可以通过上一层递归搭出来的线进行本次搭线**

      cur  --------------> cur.next

cur.left  cur.right     cur.next.left   cur.next.right

if cur.left:
cur.left.next = cur.right //操作1
if cur.right:
    if cur.next:
        cur.right.next = cur.next.left //操作2
    else : 
        cur.right.next = None
"""

class Solution():
    def connect(self,root:Optional[TreeNode])->Optional[TreeNode]:
        self.dfs(root)
        return root


    def dfs(self,node):
        #中
        if not node:
            return 
        if node.left:
            node.left.next = node.right
        if node.right:
            if node.next: # 1.节点有next
                node.right.next = node.next.left
            else: # 2. 节点next为None
                node.right.next = None
        #递归处理下一层左右孩子
        self.dfs(node.left)
        self.dfs(node.right)
        




if __name__=="__main__":
    # 构建测试用例
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # 调用 connect 方法
    solution = Solution()
    solution.connect(root)

    # 打印结果
    def print_tree_next(node: Optional[TreeNode]):
        while node:
            cur = node
            while cur:
                print(cur.val, end=" -> ")
                cur = cur.next
            print("None")
            node = node.left

    print_tree_next(root)


            
