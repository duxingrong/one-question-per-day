/*
替换数字
给定一个字符串
s，它包含小写字母和数字字符，请编写一个函数，将字符串中的字母字符保持不变，而将每个数字字符替换为number
C++不允许使用额外的空间
 */

#include <iostream>
#include <string>
using namespace std;
class Solution {
public:
  string function(string &s) {
    int left = s.size() - 1;
    int count = 0;
    for (const char val : s) {
      if (val >= '0' and val <= '9') {
        count++;
      }
    }
    s.resize(s.size() + count * 5);
    int right = s.size() - 1;
    while (left >= 0) {
      if (s[left] >= '0' and s[left] <= '9') {
        s[right--] = 'r';
        s[right--] = 'e';
        s[right--] = 'b';
        s[right--] = 'm';
        s[right--] = 'u';
        s[right--] = 'n';
      } else {
        s[right--] = s[left];
      }
      left--;
    }
    return s;
  }
};

int main() {
  string s = "a1b2c3";
  Solution obj;
  string result = obj.function(s);
  cout << result << endl;
}
