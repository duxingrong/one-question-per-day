"""
删除链表中值为val的节点
"""
from typing import Optional

# 定义链表节点的类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # 节点存储的值
        self.next = next  # 指向下一个节点的指针

# 定义解决链表问题的类
class Solution:
    # 移除链表中值为val的所有节点
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #Optional[ListNode] 表示这个参数可以是 ListNode 类型的对象，也可以是 None（即链表为空）
        
        # 创建虚拟头部节点，它的next指向head，这样我们就不需要特殊处理头节点的删除
        dummy_head = ListNode(next=head)
        
        # current指针从虚拟头节点开始遍历
        current = dummy_head
        
        # 遍历链表，直到current.next为空（即到达链表尾部）
        while current.next:
            # 如果current.next的值等于val，则删除该节点
            if current.next.val == val:
                # 将current.next指向下一个节点的下一个节点，即删除current.next节点
                current.next = current.next.next
            else:
                # 如果current.next的值不等于val，则current指针向前移动一位
                current = current.next
        
        # 返回虚拟头节点的下一个节点，即新链表的头节点
        return dummy_head.next

# 辅助函数，用于打印链表
def print_list(node):
    while node:  # 遍历链表直到最后一个节点
        print(node.val, end=" -> ")  # 打印当前节点的值，并添加箭头分隔符
        node = node.next  # 移动到下一个节点
    print("None")  # 打印完所有节点后，打印"None"表示链表的结束

# 创建链表并初始化一些节点
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(6)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(6)

# 构建链表：node1 -> node2 -> node3 -> node4 -> node5 -> node6
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

# 打印原始链表
print("Original list:")
print_list(node1)

# 创建Solution实例并调用removeElements方法
solution = Solution()
new_head = solution.removeElements(node1, 6)  # 删除值为6的节点

# 打印删除特定值后的链表
print("List after removing value 6:")
print_list(new_head)

