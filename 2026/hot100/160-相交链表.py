"""
160. 相交链表

给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null

"""

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        pA = headA
        pB = headB

        while pA is not pB:
            pA = pA.next if pA is not None else headB
            pB = pB.next if pB is not None else headA


        return pA  # 最后即使没有，两个也会在最后的地方为None 