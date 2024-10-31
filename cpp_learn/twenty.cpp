/*
当操作为1时，表示有人已经取走奶茶，从队列中删除该人的信息
当操作为2时，表示有新人加入排队，将该人的信息加入队列
在一系列的操作后，你需要回答:下一个取奶茶的人是谁

输入描述:
第一行有一个整数n,代表初始队列有n个人
第二行有n个字符串，代表当前奶茶队列中的人
第三行为一个整数m,代表接下来将会有m次操作
当操作为1时，表示有人已经取走奶茶，从队列中删除该人的信息
当操作为2时，表示有新人加入排队，将该人的信息加入队列

输出描述
输出只有一行，为下一个取奶茶的人，如果已经没有取奶茶的人了，输出"There are no
more prople in the queue."
*/

#include <iostream>
#include <queue>
#include <string>
int main() {
  int n;
  std::cin >> n;
  std::queue<std::string> q;
  while (n--) {
    std::string data;
    std::cin >> data;
    q.push(data);
  }
  int m;
  std::cin >> m;
  while (m--) {
    int a;
    std::cin >> a;
    if (a == 1) {
      if (q.size() != 0)
        q.pop();
      continue;
    } else {
      std::string b;
      std::cin >> b;
      q.push(b);
    }
  }
  if (q.empty())
    std::cout << "There are no more people in the queue.";
  else
    std::cout << q.front() << std::endl;
}
