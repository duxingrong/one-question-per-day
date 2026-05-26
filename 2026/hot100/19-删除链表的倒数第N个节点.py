"""
19. 删除链表的倒数第 N 个结点

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点

"""


"""
利用快慢指针，让fast 先走n+1步，为什么加1是因为我们要删除倒数第N个，那就是需要在倒数N+1个这里删除
"""

from typing import Optional 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head 

        fast = dummy 
        slow = dummy 


        for _ in range(n+1):
            fast = fast.next 

        while fast : 
            fast = fast.next 
            slow = slow.next 

        
        # 开删
        slow.next = slow.next.next 

        return dummy.next 