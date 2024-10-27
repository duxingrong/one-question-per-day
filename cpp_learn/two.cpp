/*
计算a+b,但输入方式有所改变，第一行是一个整数N，表示后面会有N行a和b,通过空格隔开
对于输入的每一对a和b,你需要在相应的行输出a,b的和，如果第二对a和b，对应的和也输出在第二行
输入:
2
2 4
9 21

输出:
6
30
*/

#include <iostream>
int main() {
  int N;
  int a, b;
  while (std::cin >> N) {
    for (int i = 0; i < N; i++) {
      std::cin >> a >> b;
      int result = a + b;
      std::cout << result << std::endl;
    }
  }
  return 0;
}

// 也可以两个while循环
#include <iostream>
int main() {
  int N, a, b;
  while (std::cin >> N) {
    while (N--) {
      std::cin >> a >> b;
      int result = a + b;
      std::cout << result << std::endl;
    }
  }
}
