"""
K个一组翻转链表

给你链表的头节点head,每k个节点一组进行翻转,请你返回修改后的链表

k是一个正整数,它的值小于或等于链表的长度,如果节点总数不是k的整数倍,那么请将最后剩余的节点保持原有的顺序

你不能只是单纯的改变节点内部的值,而是需要实际进行节点交换

将翻转链表和判断长度封装,然后注重前后每个翻转组的连接

"""

from typing import Optional

class ListNode():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next =next

class Solution():
    def reverseKGroup(self,head:Optional[ListNode],k:int)->Optional[ListNode]:

        def has_k_nodes(start,k):
            count=0
            while start and count<k:
                start=start.next
                count+=1
            return count==k

        def reverse_linked_list(start,end):
            prev =None
            curr = start
            while curr!=end:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev

        # 特殊情况
        if head is None:
            return head

        # 创建虚拟头节点
        dummy = ListNode()
        dummy.next = head

        group_prev = dummy

        while head:

            # 首先判断长度是否能反转
            if not has_k_nodes(head,k):
                break

            # 如果可以
            group_start = head
            group_end = head
            ## 找到start_end
            for i in range(k-1):
                group_end = group_end.next

            ## 保存下一组的开始节点
            next_group_head = group_end.next

            ## 开始反转start-end
            group_prev.next = reverse_linked_list(group_start,group_end.next)

            ## 与后面的链表衔接起来,因为反转,start才是末尾
            group_start.next = next_group_head

            ## 更新
            group_prev = group_start
            head = next_group_head

        return dummy.next
            





        
