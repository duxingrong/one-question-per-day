"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 None 。
"""
"""
基本上没有什么难点。就在于知道，怎么确定有没有交点，先将两个链表长的那个与短的对齐，然后再判断想不相等，相等即是有交点，第一次相等便是起始交点。
"""
class ListNode():
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 计算两个链表的长度
        lenA, lenB = self.getLength(headA), self.getLength(headB)
        
        # 移动较长链表的头，使其长度与较短链表相等
        dis = lenA - lenB
        if dis > 0:
            for _ in range(dis):
                headA = headA.next
        else:
            for _ in range(-dis):
                headB = headB.next
        
        # 同时遍历两个链表，直到找到相交节点或到达末尾
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        # 如果没有找到交点，返回 None
        return None

    def getLength(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

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
print_List(node3)

solution=Solution()
intersection=solution.getIntersectionNode(node1,node3)
print(intersection.val)