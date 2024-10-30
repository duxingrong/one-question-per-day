/*
构建一个单向链表，链表中包含一组整数数据。输出链表中的所有元素
要求:
1. 使用自定义的链表数据结构
2. 提供一个linkedList类来管理链表，包含构建链表和输出链表元素的方法
3.
在main函数中，创建一个包含一组整数数据的链表，然后调用链表的输出方法将所有的元素打印出来

输入描述:
包含多组测试数据，输入直到文件尾结束
每组的第一行包含一个整数n，表示需要构建的链表的长度
接下来一行包含n个整数，表示链表中的元素

输出描述:
每组测试数据输出占一行
按照顺序打印出来链表中的元素，每个元素后面跟上一个空格

5
1 2 3 4 5
6
3 4 5 6 7 8

输出
1 2 3 4 5
3 4 5 6 7 8
 */

// 定义结构体和初始化
#include <iostream>
struct ListNode {
  int val;
  ListNode *next;

  ListNode(int data) : val(data), next(nullptr) {}
};

int main() {
  // 一般都会为链表创建一个虚拟的头节点
  ListNode *dummyHead = new ListNode(0);
  int n, val;
  while (std::cin >> n) {
    ListNode *cur = dummyHead; // 定义一个临时变量来构造链表
    for (int i = 0; i < n; i++) {
      std::cin >> val;
      ListNode *newNode = new ListNode(val);
      cur->next = newNode;
      cur = cur->next;
    }
    // 遍历输出
    cur = dummyHead;
    while (cur->next != NULL) {
      std::cout << cur->next->val << " ";
      cur = cur->next;
    }
    std::cout << std::endl;
  }
}
