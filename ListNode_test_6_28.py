"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
1->2->3->4
2->1->4->3
"""
# 递归版本
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # 待翻转的两个node分别是pre和cur
        pre = head
        cur = head.next
        next = head.next.next
        
        cur.next = pre  # 交换
        pre.next = self.swapPairs(next) # 将以next为head的后续链表两两交换
         
        return cur


def print_List(node):
    while node:
        print(node.val,end=' -> ')
        node=node.next
    print('None')
    


# 创建链表 1 -> 2 -> 3 -> 4 -> 5
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
print_List(node1)


solution=Solution()
new_head=solution.swapPairs(node1)
print_List(new_head)

#递归真的很神奇