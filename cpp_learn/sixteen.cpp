/*
给定一个只包含小写字母的字符串，统计字符串中每个字母出现的频率，并找出出现频率最高的字母，如果最高的频率字母有多个，输出字典序列靠前的那个字母

输入描述:
包含多组测试数据，每组测试数据占一行

输出描述:
有多组输出，每组输出占一行

这就是一个典型的哈希表
*/

#include <iostream>
#include <string>
int main() {
  int n;
  std::cin >> n;
  while (n--) {
    std::string s;
    std::cin >> s;
    int arr[26] = {0};
    int result = 0;
    for (int i = 0; i < s.size(); i++) {
      arr[s[i] - 97] += 1;
      result = std::max(result, arr[s[i] - 97]);
    }
    for (int i = 0; i < 26; i++) {
      if (arr[i] == result) {
        char ans = i + 'a';
        std::cout << ans << std::endl;
        break;
      }
    }
  }
}
