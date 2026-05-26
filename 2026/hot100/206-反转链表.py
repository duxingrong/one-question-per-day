"""

206. 反转链表

给你单链表的头节点 head ，请你反转链表，并返回反转后的链表

"""


"""
保存下一个
反转当前指针
prev 前进
cur 前进
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None 
        cur = head 

        while cur is not None: 

            next_node = cur.next  # 保存当前节点的下一个节点

            cur.next = prev # 将当前节点反向

            prev = cur  # prev 往前走

            cur = next_node # cur 往前走 

        return prev 