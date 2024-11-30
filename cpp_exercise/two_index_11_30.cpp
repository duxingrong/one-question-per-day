/*
反转字符串

编写一个函数，将输入的字符串反转过来,输入的字符串一字符数组char[]的形式给出

原地修改数组

 */
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
  vector<char> reverseString(vector<char> &s) {
    int left = 0;
    int right = s.size() - 1;
    while (left < right) {
      swap(s[left], s[right]);
      left++;
      right--;
    }
    return s;
  }
};

int main() {
  vector<char> s = {'h', 'e', 'l', 'l', 'o'};
  Solution obj;
  obj.reverseString(s);
  for (const char i : s) {
    cout << i << " ";
  }
}
