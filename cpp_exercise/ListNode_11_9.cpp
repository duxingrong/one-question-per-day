/*
反转一个单链表
*/
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int data) : val(data), next(nullptr) {}
};
class Solution {
public:
  ListNode *reverseList(ListNode *head) {
    ListNode *cur = head;
    ListNode *pre = nullptr;
    while (cur != nullptr) {
      ListNode *tmp = cur->next;
      cur->next = pre;
      pre = cur;
      cur = tmp;
    }
    return pre;
  };
};
