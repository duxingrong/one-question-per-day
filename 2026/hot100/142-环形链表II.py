"""
142. 环形链表 II

给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表

"""


"""
慢走了a+b 

快走了a+b+n(b+c) 因为快指针可能在圈里饶了n圈

然后fast  = 2 slow 即 : a+b+n(b+c) = 2a +2b 

a  = n(b+c) - b = (n-1)(b+c) + c 

从head 走到入环点需要a步。而从相遇点M继续走c步，也刚好到环点,多出来的 (n - 1)(b + c) 只是多绕了几圈，不影响最后位置


一个指针从 head 出发
一个指针从相遇点 M 出发

它们每次都走一步
最后一定会在入环点 E 相遇
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast  = head 
        slow = head 

        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next 

            if fast is  slow:
                p1 = head 
                p2 = slow 

                while p1 is not  p2:
                    p1 = p1.next
                    p2 = p2.next
                
                return p1 
            
        return None 
    
