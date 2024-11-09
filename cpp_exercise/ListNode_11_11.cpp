/*
给你一个链表，删除链表的倒数第n个节点，并且返回链表的头节点

使用一趟扫描实现

双指针的经典应用
删除倒数第n个节点，就是fast和slow之间要隔几个节点,这样当fast==Nullptr时，slow刚好在倒数第n个节点的前一个节点
*/

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int data) : val(data), next(nullptr) {}
};

class Solution {
public:
  ListNode *removeNthFromEnd(ListNode *head, int n) {
    // 创建虚拟头节点
    ListNode *dummyhead = new ListNode(0);
    dummyhead->next = head;
    // 创建双指针
    ListNode *slow = dummyhead;
    ListNode *fast = dummyhead;
    for (int i = 0; i < n + 1; i++) {
      if (fast != nullptr) // 这个条件是为了防止操作空指针
        fast = fast->next;
    }
    while (fast != nullptr) {
      fast = fast->next;
      slow = slow->next;
    }
    // 手动删除内存
    ListNode *tmp = slow->next;
    slow->next = slow->next->next;
    delete tmp;

    return dummyhead->next;
  };
};
