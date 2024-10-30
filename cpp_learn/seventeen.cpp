/*
请你编写一个程序，判断给定的整数n是否存在于给定的集合中

输入描述:
有多组测试数据，第一行有一个整数k,代表有k组测试数据
每组数据第一行首先是一个正整数m,表示集合中元素的数量
接下来一行包含m个整数，表示集合中的元素.
最后一行包含一个整数n,表示需要进行判断的目标整数

输出描述:
包含多组输出，每组输出占一行
如果集合中存在m，输出"YES",否则输出"NO"
*/

#include <iostream>
#include <set>
int main() {
  int n;
  std::cin >> n;
  while (n--) {
    int m;
    std::cin >> m;
    std::set<int> mySet;
    while (m--) {
      int data;
      std::cin >> data;
      mySet.insert(data);
    }
    int val;
    std::cin >> val;
    if (mySet.find(val) != mySet.end()) {
      std::cout << "YES" << std::endl;
    } else {
      std::cout << "NO" << std::endl;
    }
  }
}
