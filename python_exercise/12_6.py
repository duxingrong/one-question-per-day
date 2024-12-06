"""
环形链表
给定一个链表，判断链表中是否有环

如果链表中有某个节点，可以通过连续追踪next指针再次到达，则链表中存在环
为了表示给定链表中的环，我们使用整数pos来表示链表尾部连接到链表中的位置
(索引从0开始)，如果pos是-1,则在该链表中没有环，注意:pos不作为参数进行传递，
仅仅是为了识别链表的实际情况

如果链表中存在环，则返回true，否则，返回false
"""


"""
快慢指针，fast每次走两步，slow每次一步，如果她两相遇了，证明一定有环
"""

class ListNode():
    def __init__(self,val=0,next = None):
        self.val = val 
        self.next = next 


class Solution():
    def hasCycle(self,head:ListNode)->bool:
        fast,slow = head,head 
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 
            if fast == slow :
                return True 
        return False

"""
如果要返回环的入口界节点，之前也做过

x: 起点到入口
y: 入口到相遇节点
z: 相遇节点到入口
由公式 x+y + n(y+z) == 2*(x+y)   n>=1 因为相遇一定是fast转了一圈或者更多
从公式如果n = 1 ,那么就有 x=z 
说明从相遇出发，从起点出发，相遇点就是入口！
n>1 对这个没影响，只是fast在没相遇前多跑了一些路程
"""

class Solution():
    def detectCycle(self,head:ListNode)->ListNode :
        fast = slow = head 
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next 
            if fast == slow:
                fast = head #重置fast 
                while fast != slow :
                    fast = fast.next 
                    slow = slow.next 
                return slow
        return None   
        

