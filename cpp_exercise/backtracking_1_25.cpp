/*

分割回文串

给定一个字符串s，将s分割成一些子串，使得每个子串都是回文串

返回s所有可能的分割方案

输入"aab" 输出:[["aa","b"],["a","a",'b']]

利用递归来不断分割

*/

#include <string>
#include <vector>
using namespace std;
class Solution {
private:
  vector<vector<string>> result;
  vector<string> path;
  bool isPalindrome(const string &s, int start, int end) {
    for (int i = start, j = end; i < j; i++, j--) {
      if (s[i] != s[j]) {
        return false;
      }
    }
    return true;
  }
  void backtracking(string s, int startIndex) {
    // 最简单的递归
    if (startIndex == s.size()) {
      result.push_back(path);
      return;
    }
    //一般的逻辑
    for (int i = startIndex; i < s.size(); i++) {
      //如果是回文串，继续递归
      if (isPalindrome(s, startIndex, i)) {
        //截取子串
        string str = s.substr(startIndex, i - startIndex + 1);
        path.push_back(str);
        backtracking(s, i + 1); //递归去从i+1开始继续分割
        path.pop_back();        //回溯
      }
    }
  }

public:
  vector<vector<string>> partition(string &s) {
    result.clear();
    path.clear();
    backtracking(s, 0);
    return result;
  }
};
