/*
给定一个长度为偶数位的字符串，请编程实现字符串的函数位置互换

输入包含多组测试数据
输入的第一行是一个整数n，表示有测试数据(整个输入中，只有一个n)
接下来是n组测试数据，保证串长为偶数位(串长<=50)


输出描述
请为每组测试数据输出奇偶位置互换后的结果，每组输出占一行

举例:
2
0aa0
bb00

a00a
bb00
*/

#include <iostream>
#include <string>

void swap(char &a, char &b) {
  char val = a;
  a = b;
  b = val;
}

int main() {
  int n;
  std::cin >> n; // 读取时会自动跳过换行符号,不需要加上getchar()
  while (n--) {
    // 记录数据
    std::string s;
    std::cin >> s;
    // 如何实现位置互换
    for (int i = 0; i < s.size() - 1; i += 2) {
      // std::swap(s[i], s[i + 1]);
      // int val = 0;
      // val = s[i];
      // s[i] = s[i + 1];
      // s[i + 1] = val;
      swap(s[i], s[i + 1]);
    }
    std::cout << s << std::endl;
  }
}
