/*
翻转字符串2

给定一个字符串s和一个整数k，从字符串开头算起，每计数至2k个字符，就反转这2k个字符中的前k个字符
如果剩余字符少于k个，则将剩余的字符全部反转
如果剩余字符小于2k但是大于或者等于k个，则反转前k个字符，其余字符保持原样.

s="abcdefg" k=2
"bacdfeg"

 */
#include <string>
using namespace std;
class Solution {
public:
  string reverseStr(string &str, int k) {
    for (int i = 0; i < str.size(); i += (2 * k)) {
      // 怎么说呢，只是说以2k为单位处理，实际上每次都只处理k个
      if (i + k <= str.size() - 1) {
        reverse(str, i, i + k - 1);
        continue;
      }
      // 如果发现遍历的这一次的2k中的数字小于了k个，全部反转
      reverse(str, i, str.size() - 1);
    }
    return str;
  }

  void reverse(string &str, int start, int end) {
    int left = start;
    int right = end;
    while (left < right) {
      swap(str[left], str[right]);
      left++;
      right--;
    }
  }
};
