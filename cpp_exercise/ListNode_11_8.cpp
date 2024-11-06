/*
在链表中实现这些功能
get(index):获取链表中第index个节点的值，如果索引无效，则返回-1
addAtHead(val):在连表的第一个元素之前添加一个值为val的节点，插入后，新节点将成为链表的第一个节点
addAtIndex(index,val):在链表中的第index个节点之前添加值为val的节点，如果index等于链表的长度，则该节点将附加到链表的末尾，如果index大于链表长度，则不会插入节点。如果index小于0,则在头部插入节点
deleteAtIndex(index):如果索引index有效，则删除链表的第index个节点
*/

#include <iostream>
class MyLinkedList {
public:
  struct ListNode {
    int val;
    ListNode *next;
    ListNode(int data) : val(data), next(nullptr) {}
  };

  // 初始化链表
  MyLinkedList() {
    dummyHead = new ListNode{0};
    length = 0;
  }
  // 得到节点的值
  int get(int index) {
    if (index >= length)
      return -1;
    else {
      ListNode *cur = dummyHead->next;
      while (index--) {
        cur = cur->next;
      }
      return cur->val;
    }
  };
  // 增加头节点
  void addAtHead(int val) {
    ListNode *newNode = new ListNode(val);
    ListNode *tmp = dummyHead->next;
    dummyHead->next = newNode;
    newNode->next = tmp;
    length++;
  }
  // 增加尾节点
  void addAtTail(int val) {
    ListNode *cur = dummyHead;
    while (cur->next != nullptr) {
      cur = cur->next;
    }
    ListNode *newNode = new ListNode(val);
    cur->next = newNode;
    length++;
  }
  // 添加节点,新插入的节点的index是0的话，就是新添加了头节点,是1的话，就是它成为新的1节点,链表节点从0开始数
  void addAtIndex(int index, int val) {
    if (index < 0) {
      index = 0;
    } else if (index > length) {
      return;
    }
    ListNode *cur = dummyHead;
    while (index--) {
      cur = cur->next;
    }
    ListNode *newNode = new ListNode(val);
    newNode->next = cur->next;
    cur->next = newNode;
    length++;
  }
  // 去除节点
  void deleteAtIndex(int index) {
    if (length <= index or index < 0) {
      return;
    }
    ListNode *cur = dummyHead;
    while (index--) {
      cur = cur->next;
    }
    ListNode *tmp = cur->next;
    cur->next = cur->next->next;
    length--;
    delete tmp;
    tmp = nullptr;
  }

  void printList() {
    ListNode *cur = dummyHead;
    while (cur->next != nullptr) {
      std::cout << cur->next->val << " ";
      cur = cur->next;
    }
    std::cout << std::endl;
  }

private:
  int length;
  ListNode *dummyHead;
};
