/*
请编写一个程序，实现以下的链表操作：构建一个单向链表，链表中包含一组整数数据
1. 实现在链表第n个位置插入一个元素，输出整个链表的所有元素
2. 实现删除链表的第m个位置的元素，输出整个链表的所有元素

要求:
使用自定义的链表数据结构
提供一个linkedList类来管理链表，包含构建链表，插入元素，删除元素和输出链表元素的方法
在main函数中，创建一个包含一组整数数据的链表，然后根据输入的n和m，调用链表的方法插入和删除元素，并输出整个链表的所有元素

输入描述:
每次输出只有一组测试数据
每组的第一行包含一个整数k，表示需要构建的链表的长度
第二行包含k个整数，表示链表中的元素
第三行包含一个整数s，表示后续会有s行输入，每行两个整数，第一个整数为n，第二个整数为x，代表在链表的第n个位置插入x
在s行输入后，后续会输入一个整数L,表示后续会有L行输入，每行一个整数m,代表删除链表中的第m个元素

输出描述:
每组第一行输出构建的链表，链表元素中用空格隔开，最后一个元素后没有空格。
然后是S行输出，每次插入一个元素之后都将链表输出一次，元素之间用空格隔开，最后一个元素后没有空格；
如果插入位置不合法，则输出“Insertion position is invalid.”。
然后是L行输出，每次删除一个元素之后都将链表输出一次，元素之间用空格隔开，最后一个元素后没有空格；如果删除元素后链表的长度为0，则不打印链表。
如果删除位置不合法，则输出“Deletion position is invalid.”。
如果链表已经为空，执行删除操作时不需要打印任何数据。
*/

#include <iostream>

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int data) : val(data), next(nullptr) {}
};
// 创建一个打印链表的函数
void printLinklist(ListNode *Head) {
  ListNode *cur = Head;
  while (cur->next != NULL) {
    std::cout << cur->next->val << " ";
    cur = cur->next;
  }
  std::cout << std::endl;
}
// 主函数
int main() {
  int k;
  std::cin >> k;
  int listLen = k; // 代表链表的长度
  // 创建链表
  ListNode *dummyHead = new ListNode(0);
  ListNode *cur = dummyHead;
  for (int i = 0; i < k; i++) {
    int data;
    std::cin >> data;
    ListNode *newNode = new ListNode(data);
    cur->next = newNode;
    cur = cur->next;
  }

  int s; // s代表要执行几次插入
  std::cin >> s;
  while (s--) {
    int n, x;
    std::cin >> n >> x;
    // 判断合法性
    if (n <= 0 || n > listLen) {
      std::cout << "Insertion position is invalid." << std::endl;
      continue;
    } else {
      cur = dummyHead;
      // 开始插入
      for (int i = 1; i < n; i++) {
        cur = cur->next;
      }
      ListNode *newNode = new ListNode(x);
      ListNode *tmp = cur->next;
      cur->next = newNode;
      newNode->next = tmp;
      listLen += 1;
      printLinklist(dummyHead);
    }
  }
  int L;
  std::cin >> L;
  while (L--) {
    int m;
    std::cin >> m;
    // 判断合法性
    if (m <= 0 || m > listLen) {
      std::cout << "Deletion position is invalid." << std::endl;
      continue;
    } else {
      // 开始删除
      cur = dummyHead;
      for (int i = 1; i < m; i++) {
        cur = cur->next;
      }
      cur->next = cur->next->next;
      listLen -= 1;
      if (listLen != 0)
        printLinklist(dummyHead);
    }
  }
}
