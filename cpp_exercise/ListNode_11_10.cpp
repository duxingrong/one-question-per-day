/*

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表

你不能只是单纯改变节点内部的值，而是需要实际的进行节点交换

这个题目难点在于分而治之，只要每次变换两个节点就好

*/
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int data) : val(data), next(nullptr) {}
};

class Solution {
public:
  ListNode *swapPairs(ListNode *head) {

    ListNode *dummyhead = new ListNode(0); // 头节点
    dummyhead->next = head;
    ListNode *cur = dummyhead;
    while (cur->next != nullptr && cur->next->next != nullptr) {
      ListNode *first = cur->next;
      ListNode *second = cur->next->next; // 这里是nullptr也没有关系

      // 开始变换
      first->next = second->next;
      second->next = first;
      cur->next = second;
      cur = first; // 这里的first是最初的cur->next->next->next
    }
    return dummyhead->next;
  };
};
