/*
 右旋字符串

 字符串的右旋操作是把字符串尾部的若干个字符转移到字符串的前面，给定一个字符串s和一个正整数k,请编写一个函数，将字符串中的后面k个字符转移到字符串的前面，实现字符串的右旋转操作

输入:输入共包含两行，第一行为一个正整数k,代表右旋转的位数。第二行为字符串s,代表需要旋转的字符串

输出:输出共一行，为进行了右旋转操作的字符串



这个题目关键就在于反转再反转，做过一次就知道了

 */
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;
class Solution {
public:
  string function(string &s, int k) {
    // 首先将整个字符串反转
    reverse(s.begin(), s.end());
    // 然后反转前k个字符
    reverse(s.begin(), s.begin() + k); // 前k个元素
    reverse(s.begin() + k, s.end());   // 索引从0开始，下标k开始(包括k)
    return s;
  }
};

int main() {
  int k;
  cin >> k;
  string s;
  cin >> s;
  Solution obj;
  string result = obj.function(s, k);
  cout << result << endl;
}
