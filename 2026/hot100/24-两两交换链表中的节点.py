"""
24. 两两交换链表中的节点

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）

"""



from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)

        prev = dummy 

        while prev.next and prev.next.next:

            a = prev.next 
            b = prev.next.next 

            # 下一组的开头
            next_pair = b.next 

            # 开始交换
            a.next = next_pair 
            b.next = a 
            prev.next = b 

            # prev 移动到交换后的这一组的末尾，也就是a 
            prev = a 

        return dummy.next 