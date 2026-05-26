"""
21. 合并两个有序链表

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的

"""


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 虚拟头节点，不存真正结果，只是方便拼接
        dummy = ListNode(0)

        # cur 用来指向当前新链表中的最后一个节点
        cur = dummy 


        pA = list1 
        pB = list2 

        while pA and  pB: 
            if pA.val < pB.val :
                cur.next = pA 
                pA = pA.next 
            
            else:
                cur.next = pB 
                pB = pB.next

            cur = cur.next 

        if pA :
            cur.next = pA 
        
        if pB : 
            cur.next = pB 

        return dummy.next 
    