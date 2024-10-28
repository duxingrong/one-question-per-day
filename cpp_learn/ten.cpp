/*
每门课的成绩分别为A，B，C，D，F五个等级，为了计算平均绩点,规定A，B，C，D，F分别代表4分，3分，2分，1分，0分

输入描述:
有多组测试样例，每组输入数据占一行，由一个或多个大写的字母组成，字母之间由空格分隔

输出描述:
每组输出结果占一行，如果输入的大写字母都在集合{A,B,C,D,F}中，输出平均绩点,否则输出unknown
*/

// 怎么判断他输入完了一行呢?  函数getline()
// 以及将字母和数字相联系  直接笨方法
//
#include <iostream>
#include <stdio.h>
#include <string>
int main() {
  std::string s;
  while (std::getline(std::cin, s)) { // 一直接收字符，知道换行
    float sum = 0;
    int count = 0;
    int flag = 1;
    for (int i = 0; i < s.size(); i++) {
      if (s[i] == 'A') {
        sum += 4;
        count += 1;
      } else if (s[i] == 'B') {
        sum += 3;
        count += 1;
      } else if (s[i] == 'C') {
        sum += 2;
        count += 1;
      } else if (s[i] == 'D') {
        sum += 1;
        count += 1;
      } else if (s[i] == 'F') {
        sum += 0;
        count += 1;
      } else if (s[i] == ' ')
        continue;
      else {
        flag = 0;
        std::cout << "Unknown" << std::endl;
        break;
      }
    }
    if (flag) {
      printf("%.2f\n", sum / count);
    }
  }
  return 0;
}
