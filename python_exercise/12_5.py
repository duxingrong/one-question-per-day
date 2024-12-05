"""
重排链表
给定一个链表的头节点Head,链表为L0->L1->L2->L3....
将链表重新排列为L0->Ln->L1->Ln-1....
"""




class ListNode():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

"""
方法一: 将链表放进数组中，一前一后构造链表
"""
class Solution():
    def reorderList(self,head:ListNode)->None:
        #将链表放进数组
        cur  = head
        nums = []
        while cur:
            nums.append(cur.val)
            cur = cur.next

        #现在利用双指针，制造链表
        left = 1
        right = len(nums)-1
        cur = head
        flag = 1
        while left<=right:
            if flag ==0:#标志是添加left
                cur.next = ListNode(nums[left])
                left+=1
                flag = 1
                cur = cur.next
            else: 
                cur.next = ListNode(nums[right])
                right-=1
                flag = 0
                cur = cur.next
        
"""
方法二，使用昨天的反转链表，先将后半部分反转，然后重新排列
"""

class Solution():
    def reorderList(self,head:ListNode)->None:
        if head==None or head.next == None :
            return True
        #快慢指针
        fast , slow = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        right = slow.next  #分割右半边
        slow.next = None #切断,这里从slow.next当作right很重要，因为这样才能保证右边长度一定小于左边
        right = self.reverseList(right)#返转右半边
        left = head 
        while right:
            curLeft = left.next 
            left.next = right 
            left = curLeft

            curRight = right.next 
            right.next = left 
            right = curRight


    def reverseList(self,head:ListNode)->ListNode:
        cur = head 
        pre = None 
        while (cur!= None ):
            tmp = cur.next 
            cur.next  = pre 
            pre = cur 
            cur = tmp 
        return pre 

    


"""
将链表放入双向队列中
"""
from collections import deque 


class Solution():
    def reorderList(self,head:ListNode)->None:
        #将链表放进数组
        cur  = head
        nums = deque()
        while cur:
            nums.append(cur.val)
            cur = cur.next

        nums.popleft()#先弹出第一个，因为是head

        while nums:
            head.next = ListNode(nums.pop())
            if not nums:
                break
            head.next.next = ListNode(nums.popleft())
            head = head.next.next

        