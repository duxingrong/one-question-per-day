"""
两两交换链表中的节点

给定一个链表，两两将交换其中相邻的节点，并返回交换后的链表

你不能只是单纯改变节点内部的值，而是需要实际的进行节点交换
"""

#链表
class ListNode():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


class Solution():
    def swapPairs(self,head:ListNode)->ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head
        cur = dummy_head
        while cur.next!=None and cur.next.next!=None:
            #储存值,为后面的交换做准备
            tmp1 = cur.next
            tmp2 = cur.next.next.next 

            #开始交换
            cur.next = cur.next.next
            cur.next.next = tmp1
            cur.next.next.next = tmp2
            
            #下一轮交换
            cur = cur.next.next

        return dummy_head.next



            
            
        
