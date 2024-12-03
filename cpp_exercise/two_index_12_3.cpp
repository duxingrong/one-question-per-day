/*
反转链表
1->2->3->4->5->NULL
5->4->3->2->1->NULL
*/

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int data) : val(data), next(nullptr) {};
};

class Solution {
public:
  ListNode *reverseList(ListNode *head) {
    ListNode *cur = head;
    ListNode *prev = nullptr;
    while (cur != nullptr) {
      // 记录下一个cur
      ListNode *tmp;
      tmp = cur->next;
      //  开始转向
      cur->next = prev;
      // 记录当前值给prev
      prev = cur;
      // 进入下一次循环
      cur = tmp;
    }
    return prev;
  }
};
