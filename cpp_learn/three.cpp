/*

 还是计算A+B,输入每行是一对a+b,其中会有一对是0和0标志着输入的结束，且这一对不要计算

 对于输入的每行a和b，你需要在相应的行输出a,b的和，第二行输入，也要在第二行输出


这里相当于我们需要主动得结束循环

 */

#include <iostream>
int main() {
  int a, b;
  while (std::cin >> a >> b) {
    if (a == 0 && b == 0)
      break;
    int result = a + b;
    std::cout << result << std::endl;
  }
  return 0;
}
