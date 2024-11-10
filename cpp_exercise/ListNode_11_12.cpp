/*

给你两个单链表的头节点headA和headB,请你找出并返回两个单链表相交的起始节点，如果两个链表没有交点，返回null
题目数据保证整个链式结构中不存在环
函数返回结果后，链表必须保持其原始结构

*/

#include <iostream>
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int data) : val(data), next(nullptr) {}
};

class Solution {
public:
  ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    // 计算长度
    ListNode *curA = headA;
    ListNode *curB = headB;
    int countA = 0, countB = 0;
    while (curA != nullptr) {
      countA += 1;
      curA = curA->next;
    }
    while (curB != nullptr) {
      countB += 1;
      curB = curB->next;
    }
    curA = headA;
    curB = headB;
    // 保证A是最长的
    if (countA < countB) {
      std::swap(countA, countB);
      std::swap(curA, curB);
    }
    int gap = countA - countB;
    while (gap--) {
      curA = curA->next;
    }
    while (curA != nullptr) {
      if (curA == curB) {
        return curA;
      } else {
        curA = curA->next;
        curB = curB->next;
      }
    }
    return NULL;
  };
};
