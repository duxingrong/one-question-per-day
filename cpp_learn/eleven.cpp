/*
输出一个词组中每个单词的首字母的大写组合

输入的第一行是一个整数n，表示一共有n组测试数据。(输入只有一个n，没有多组的输入)
接下来有n行，每组测试数据占一行，每行有一个词组，每个词组由一个或者多个单词组成；每组的单词个数不超过10个，每个单词有一个或者多个大写或小写组成；单词长度不超过10,由一个或多个空格分隔这些单词

请为每组测试数据输出规定的缩写，每组输出占一行.

1
ad dfa fgs

ADF
注意:单词 之间可能有多个空格


怎么获得每行的开头字母呢?
*/

#include <iostream>
#include <string>
/*这里我们发现小写变成大写可以封装成一个函数
返回类型是char;
名字 changeChar;
形参列表:
一般的形参列表通常包括参数类型和参数名称。参数类型表示参数的数据类型，可以是内置数据类型(整数，字符，浮点数),用户自定义的数据类型，参数名称是在函数体内部使用的名称
这里这个(char &a)引用传递，意味着函数可以修改传递给它的参数
*/
char changeChar(char &a) {
  if (a >= 'a' && a <= 'z') {
    a -= 32;
  }
  return a;
}
int main() {
  int n;
  std::cin >> n;
  std::getchar(); // 这里吸收回车不能忘记
  while (n--) {
    std::string s;
    std::getline(std::cin, s);
    std::string result;
    result += changeChar(s[0]);
    // 遍历剩下的所有
    for (int i = 1; i < s.size() - 1; i++) {
      if (s[i] == ' ' && s[i + 1] != ' ') {
        result += changeChar(s[i + 1]);
      }
    }
    std::cout << result << std::endl;
  }
  return 0;
}
