/*
替换数字
给定一个字符串s,它包含小写字母和数字字符，请编写一个函数，将字符串中的字母字符保持不变，而将每个数字字符替换为number

举例:
a1b2c3
anumberbnumbercnumber


这里的技巧:
很多数组填充类的问题，做法都是预先给数组扩容到填充后的大小，然后在从后向前进行操作
1. 这样不用申请新数组
2.从后向前填充元素，避免了从前向后填充元素时，每次添加元素都要将添加元素之后的所有元素向后移动的问题

利用双指针，i等于新数组的末尾，j等于原始数组的末尾：
如果i遍历等于char,那就直接赋值给j
如果i遍历到数字，那j就开始遍历赋值number
由于首先就进行了扩容，所以j<=i,所以j在遍历的时候直接覆盖就好
 */
#include <iostream>
#include <string>
using namespace std;
class Solution {
public:
  string change(string &s) {
    // 先进行扩容
    int count = 0;
    int old_last = s.size() - 1;
    for (int i = 0; i < s.size(); i++) {
      if (s[i] >= '0' && s[i] <= '9') {
        count++;
      }
    }
    s.resize(s.size() + count * 5);
    // 双指针遍历赋值
    int new_last = s.size() - 1;
    for (int i = old_last; i >= 0; i--) {
      if (s[i] >= '0' && s[i] <= '9') {
        s[new_last--] = 'r';
        s[new_last--] = 'e';
        s[new_last--] = 'b';
        s[new_last--] = 'm';
        s[new_last--] = 'u';
        s[new_last--] = 'n';
      } else {
        s[new_last--] = s[i];
      }
    }
    return s;
  }
};

int main() {
  string s;
  cin >> s;
  Solution obj;
  string result = obj.change(s);
  cout << result << endl;
}
