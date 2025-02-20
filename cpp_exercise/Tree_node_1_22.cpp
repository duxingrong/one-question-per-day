/*

电话号码的字母组合

给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下(与电话按键相同)。注意1不对应任何字母。

2:abc 3:def 4: ghi 5:jkl 6:mno 7:pqrs 8:tuv 9:wxyz

*/

// 1.定义一个字符串数组
// 2.backtracking函数,接受digits和startIndex,当startIndex==digits.size()的时候，将s加入到全局变量result中

#include <string>
#include <vector>
using namespace std;
class Solution {
private:
  const string letterMap[10] = {
      "",     // 0
      "",     // 1
      "abc",  // 2
      "def",  // 3
      "ghi",  // 4
      "jkl",  // 5
      "mno",  // 6
      "pqrs", // 7
      "tuv",  // 8
      "wxyz", // 9
  };

public:
  vector<string> result;
  string s;
  void backtracking(const string &digits, int startIndex) {
    //如果startIndex==digits.size(),说明此时的s通关了
    if (startIndex == digits.size()) {
      result.push_back(s);
      return;
    }
    //计算当前的所以对应的字母
    int digit = digits[startIndex] - '0'; //将index指向的数字化为整数
    string letters = letterMap[digit];    //取出对应的字母
    //递归填充s
    for (int i = 0; i < letters.size(); i++) {
      s.push_back(letters[i]);
      backtracking(digits, startIndex + 1);
      s.pop_back();
    }
  }
  vector<string> letterCombinations(string digits) {
    s.clear();
    result.clear();
    if (digits.size() == 0) {
      return result;
    }
    backtracking(digits, 0);
    return result;
  }
};
