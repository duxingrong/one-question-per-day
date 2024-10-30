/*
假设你手里有以一串钥匙，这串钥匙上每把钥匙都有一个编号，对应着一个房门的编号，现给你一个房门编号，你需要判断是否能够打开该房门

输入描述:
测试数据共有多组
第一行为一个整数s，表示共有多少组测试数据
每组第一行有一个整数n，表示钥匙串上有多少把钥匙
后面共有n行输入，每行两个整数，第一个整数k表示钥匙编号，第二个整数d表示房门编号
最后一行有一个整数x，表示需要打开的房门编号

输出描述:
输出多组，每组独占一行，如果能打开，则输出钥匙编号，不嫩打开则输出
"Can't open the door."


python中直接用字典秒了
*/

#include <iostream>
#include <map>
int main() {
  int n;
  std::cin >> n;
  while (n--) {
    int m;
    std::map<int, int> Umap;
    std::cin >> m;
    while (m--) {
      int a, b; // a是钥匙，b是房间
      std::cin >> a >> b;
      Umap[b] = a;
    }
    int tmp;
    std::cin >> tmp;
    if (Umap.find(tmp) != Umap.end()) {
      std::cout << Umap[tmp] << std::endl;
    } else {
      std::cout << "Can't open the door." << std::endl;
    }
  }
}
