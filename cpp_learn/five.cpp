/*

计算若干整数的和

输入的第一行为一个整数N，接下来N行每行先输入一个整数M，然后在同一行内输入M个整数

对于每组输入，输出M个数的和，每组输出之间输出一个空行

只需要保证每组数据间是有空行的，但两组数据间并没有空行

*/

#include <iostream>
int main() {
  int N, M;
  while (std::cin >> N) { // 这里必须要用while因为我们是持续输入
    while (N--) {
      std::cin >> M;
      int sum = 0;
      while (M--) {
        int a;
        std::cin >> a;
        sum += a;
      }
      std::cout << sum << std::endl;
      if (N > 0) // 由这里进行判断，保证每行数据之间有空行
        std::cout << std::endl;
    }
  }
  return 0;
}
