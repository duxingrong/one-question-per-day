"""
题意：反转一个单链表。
示例: 输入: 1->2->3->4->5->NULL 输出: 5->4->3->2->1->NULL
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head, None)
    def reverse(self, cur: ListNode, pre: ListNode) -> ListNode:
        if cur == None:
            return pre
        temp = cur.next
        cur.next = pre
        return self.reverse(temp, cur)



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

# 创建 Solution 实例
solution = Solution()

# 反转链表
new_head = solution.reverseList(node1)
#打印反转后的链表
print_List(new_head)