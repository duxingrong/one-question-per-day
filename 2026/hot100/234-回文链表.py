"""

234. 回文链表

给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 

"""

"""

变量 = 某个节点        不改链表
变量 = 变量.next      不改链表，只是移动指针
节点.next = 某个东西   改链表

"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """找到中点，反转后半段，再从两头往中间比"""


        # 用快慢指针找中点

        fast = head 
        slow = head 

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 

        # 将slow 后续的反转
        prev = None 
        cur = slow 

        while cur is not None: 

            next_node = cur.next

            cur.next = prev 

            prev = cur 

            cur = next_node 


        # 开始比较
        right = prev 
        left = head 

        while right is not None :
            if right.val != left.val:
                return False 
        
            right = right.next 
            left = left.next 

        
        return True 