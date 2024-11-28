/*

重复的子字符串
给定一个非空的字符串，判断它是否可以由它的子串重复多次构成，给定的字符串只含有小写英文字母，并且长度不超过10000

*/

// 移动匹配法
#include <string>
using namespace std;
class Solution {
public:
  bool repeatedSubstringPattern(string &s) {
    string t = s + s;
    t.erase(t.begin());
    t.erase(t.end() - 1);
    if (t.find(s) != std::string::npos)
      return true;
    return false;
  }
};

// kmp算法
// 如果这个字符串s是由重复子串组成，那么最长相等前后缀不包含的子串是字符串s的最小重复子串

class Solution2 {
public:
  void getNext(int *next, string &s) {
    next[0] = 0;
    int j = 0;
    for (int i = 1; i < s.size(); i++) {
      while (j > 0 && s[i] != s[j]) {
        j = next[j - 1];
      }
      if (s[i] == s[j])
        j++;
      next[i] = j;
    }
  }
  bool repeatedSubstringPattern(string &s) {
    if (s.size() == 0)
      return false;
    // 创建一个栈上数组
    int next[s.size()];
    getNext(next, s);
    int len = s.size();
    // 有最长前后缀，且剩下的部分(重复子串)可以被s整除
    if (next[len - 1] != 0 && len % (len - next[len - 1]) == 0)
      return true;
    return false;
  }
};
