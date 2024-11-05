/*

删除链表中等于给定值val的所有节点

输入: head = [1,2,6,3,4,5,6] val=6

输出: [1,2,3,4,5]

*/

// 构建链表
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int data) : val(data), next(nullptr) {}
};

class Solution {
public:
  ListNode *removeElements(ListNode *head, int val) {
    ListNode *dummyhead = new ListNode(0);
    dummyhead->next = head;
    ListNode *cur = dummyhead;
    while (cur->next != nullptr) {
      if (cur->next->val == val) {
        cur->next = cur->next->next;
      } else {
        cur = cur->next;
      }
    }
    return dummyhead->next;
  };
};
