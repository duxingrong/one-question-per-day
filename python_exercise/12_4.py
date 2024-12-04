"""
回文链表

请判断一个链表是否为回文链表

1->2->2->1 
true

1->2
false

"""

class ListNode():
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next

"""
最简单的处理,就是转化为数组
"""
class Solution():
    def isPalindrome(self,head:ListNode)->bool:
        nums = []
        cur = head
        while cur :
            nums.append(cur.val)
            cur = cur.next

        left  = 0
        right = len(nums)-1
        while left< right:
            if nums[left]!= nums[right]:
                return False
            left+=1
            right-=1
        return True
            
"""
第二种处理，就是利用快慢指针，将链表一分为二，然后反转链表后一一比对

这里很巧妙
"""
class Solution():
    def isPalindrome(self,head:ListNode)->bool:
        #首先快慢指针，找到反转的开始位置
        slow =fast =head
        while fast and fast.next :
            fast = fast.next.next 
            slow = slow.next

        #跳出循环后，slow的位置就是开始反转的起点
        node = None #node记录的是反转链表的头结点
        #因为slow = slow.next ，slow每走一步，就反转了一个节点，当slow = None 时，反转完成
        while slow :
            #赋值是同时进行的
            slow.next , slow , node = node , slow.next , slow   #也就是经过这么一次，就slwo节点完成反向，并且node节点指向新的头节点slow ,并且slow更新，为下一个节点做铺垫

        while node :
            if node.val != head.val:
                return False
            node = node.next 
            head = head.next 
        
        return True




        

