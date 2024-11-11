/*
给定一个链表，返回链表开始入环的第一个节点。如果链表无环，则返回null
为了表示给定链表中的环，使用整数pos来表示链表尾连接到链表中的位置(索引0开始)。如果pos是-1,则在该链表中没有环
不允许修改给定的链表
pos不作为参数进行传递，仅仅是为了标识链表的实际情况

大体上就是快慢指针，fast每次移动2格,slow每次移动1格,然后如果他们相遇了，就是有环

速度差和追赶机制
速度差:由于fast每次走两步，slow每次走一步，因此fast指针相对slow指针每次前进一格
距离缩短:假设fast和slow在某一时刻都进入了环中,距离差为环内部分节点数k，每轮fast都会缩短这个距离1个节点
由于相对速度的差值为1,所以每移动k次后，fast就会追上slow,他们一定会在某个节点相遇

相遇的时候:
x:头节点到环形入口
y:入口到相遇
z:相遇到入口处

slow走了x+y
fast走了x+y+n(y+z)
所以有等式 (x+y)*2 == x+y+n(y+z)
所以有x = (n-1)(y+z)+z

当n等于1的时候,x=z
这意味着:
从头节点出发一个指针，从相遇节点也出发一个指针,这两个指针每次只走一个节点,那么当这两个指针相遇的时候就是环形入口的节点
当n>1的时候也是一样的，只不过是多转了n-1圈,相遇点还是入口处

*/
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int data) : val(data), next(nullptr) {}
};

class Solution {
public:
  ListNode *detectCycle(ListNode *head) {
    ListNode *fast = head;
    ListNode *slow = head;
    while (fast != nullptr && fast->next != nullptr) {
      slow = slow->next;
      fast = fast->next->next;

      if (fast == slow) {
        ListNode *start = head;
        while (start != slow) {
          slow = slow->next;
          start = start->next;
        }
        return start;
      }
    }
    return nullptr;
  }
};
