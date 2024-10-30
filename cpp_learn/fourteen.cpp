/*
请编写一个程序，实现以下操作:
构建一个单向链表，链表中包含一组整数数据，输出链表中的第m个元素，(m从1开始计数)

要求:
使用自定义的链表数据结构
提供一个linkdList类来管理链表，包含构建链表，输出链表元素以及输出第m个元素的方法
在main函数中，创建一个包含一组整数数据的链表，然后输入m，调用链表的方法输出第m个元素

输入描述:
第一行包含两个整数n和k，n表示需要构建的链表的长度，k代表输入的m的个数
接下来一行包含n个整数，表示链表中的元素
接下来的一行包含k个整数，表示输出链表中的第m个元素

输出描述:
测试数据输出占k行
每行输出链表中的第m个元素，如果m位置不合法，则输出
'Output position out of bounds'.

5 5
1 2 3 4 5
4 3 2 9 0

4
3
2
Output position out of bounds
Output position out of bounds
*/

#include <iostream>
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int data) : val(data), next(nullptr) {}
};

int main() {
  int n, m;
  std::cin >> n >> m;
  // 构建链表
  ListNode *dummyHead = new ListNode(0);
  ListNode *cur = dummyHead;
  while (n--) {
    int data;
    std::cin >> data;
    ListNode *newNode = new ListNode(data); // 创建一个新的指针指向这个节点
    cur->next = newNode;                    // 连接链表
    cur = cur->next;                        // 更新链表末尾
  }
  // 读取m个值
  while (m--) {
    int k;
    std::cin >> k;
    cur = dummyHead;
    while (k--) {
      if (cur != NULL) {
        cur = cur->next;
      } else {
        break;
      }
    }
    if (cur == NULL || cur == dummyHead) {
      std::cout << "Output position out of bounds." << std::endl;
    } else {
      std::cout << cur->val << std::endl;
    }
  }
}
