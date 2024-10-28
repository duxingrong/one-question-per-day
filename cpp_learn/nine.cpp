/*

 编写一个程序，模拟打印一个正方形的框，程序应该接受用户输入的正整数作为正方形的边长，并打印相应大小的正方形。注意，内部为空白，外部是由'*'字符组成的框

 */

// 太时山了
// #include <iostream>
// int main() {
//   int n;
//   std::cin >> n;
//   for (int i = 0; i < n; i++) {
//     if (i == 0 || i == n - 1) {
//       for (int j = 0; j < n; j++) {
//         std::cout << "*";
//         std::cout << " ";
//       }
//       std::cout << std::endl;
//     } else {
//       for (int j = 0; j < n; j++) {
//         if (j != 0 and j != n - 1) {
//           std::cout << "  ";
//         } else {
//           std::cout << "*";
//           std::cout << " ";
//         }
//       }
//       std::cout << std::endl;
//     }
//   }
//   return 0;
// }

// 这个题目说白了，就是第一行和最后一行，第一列和最后一列打印出'*',其他都是""(空格)
#include <iostream>
int main() {
  int n;
  std::cin >> n;
  // 两层for循环
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (i == 0 || i == n - 1 || j == 0 || j == n - 1) {
        std::cout << "*";
        std::cout << " ";
      } else {
        std::cout << "  ";
      }
    }
    std::cout << std::endl;
  }
  return 0;
}
