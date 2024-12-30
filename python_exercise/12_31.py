"""
合并k个升序链表

给你一个链表数组,每个链表都已经按升序排列

请你将所有链表合并到一个升序链表中,返回合并后的链表

lists = [[1,4,5],[1,3,4],[2,6]]
输出: [1,1,2,3,4,4,5,6]

优先队列

利用堆，首先将所有的头节点放入堆中，然后弹出来,把它的下一个节点推进取，直到堆为空,刚好也就成了
"""

from typing import Optional,List
import heapq
from functools import cmp_to_key

class ListNode():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
        
    # # 重载小于运算符,当我们对两个对象进行<比较时,Python会自动调用对象的__lt__方法
    # def __lt__(self,other):
    #     return self.val<other.val

class Solution():

    def mergeKLists(self,lists:List[Optional[ListNode]])->Optional[ListNode]:
        #堆
        heap = []
        #将所有节点加入堆
        for I in lists:
            while  I: 
                heapq.heappush(heap,I.val)
                I = I.next

        #创建虚拟头节点,方便操作
        dummy_head = ListNode()
        cur = dummy_head

        while heap:
            nodeVal = heapq.heappop(heap)
            cur.next = ListNode(nodeVal)
            cur = cur.next

        return dummy_head.next


if __name__=="__main__":
    # 测试函数
    def print_linked_list(head: ListNode):
        values = []
        while head:
            values.append(str(head.val))
            head = head.next
        print("->".join(values))

    # 创建一些测试链表
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))

    lists = [list1, list2, list3]
    # 创建 Solution 实例并合并链表
    solution = Solution()
    merged_list = solution.mergeKLists(lists)

    # 打印合并后的链表
    print_linked_list(merged_list)

