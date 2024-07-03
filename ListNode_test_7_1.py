"""
题意： 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1,则在该链表中没有环。

说明：不允许修改给定的链表。
"""
"""
掌握三点
如果链表有环,那么用快慢指针法,fast和slow一定是在环内相等。
确定有环,那我们先让fast向前走一步,初始length为1,再让fast=slow,即走了一圈,可以累计出长度
当fast=slow时,我们将指针slow重置为head,两者再次相遇的节点就是环入口节点
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode)->ListNode:
        slow = head  # 初始化慢指针
        fast = head  # 初始化快指针

        # 使用快慢指针法检测链表中是否存在环
        while fast and fast.next:
            slow = slow.next  # 慢指针向前移动一步
            fast = fast.next.next  # 快指针向前移动两步

            # 如果快慢指针相遇，说明链表中有环
            if slow == fast:
                # 计算环的长度
                cycle_length = 1
                fast = fast.next  # 将fast移动到环的下一个节点
                while fast != slow:  # 遍历环直到再次遇到slow指针
                    fast = fast.next
                    cycle_length += 1

                # 打印环的长度
                print("Length of cycle:", cycle_length)

                # 将慢指针移回链表头部
                slow = head
                # 当慢指针和快指针再次相遇时，相遇点即为环的入口节点
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                # 返回环的入口节点
                return slow

        # 如果快指针到达链表末尾，说明链表中无环
        return None

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
node5.next=node2
solution=Solution()
entrance=solution.detectCycle(node1)
print('环入口节点的值',entrance.val)


