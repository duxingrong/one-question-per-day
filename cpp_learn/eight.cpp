/*
有一天，小明收到一张很奇怪的信，信上说要小明计算出给定数各个位上数字为偶数的和

输入描述:
输入数据有多组，每组占一行，只有一个整数，保证数字在32位整型范围内

输出描述:
对于每组输入数据，输出一行，每组数据下方有一个空行

415326
3262

12

19
 */

#include <iostream>
int main() {
  int a, n;
  while (std::cin >> a) {
    int sum = 0;
    while (a != 0) {
      n = a % 10; // 取最后一位的值
      a = a / 10; // 直接缩小一位，方便下次获取
      if (n % 2 == 0)
        sum += n;
    }
    std::cout << sum << std::endl;
    std::cout << std::endl;
  }
  return 0;
}
