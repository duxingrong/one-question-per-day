/*

复原IP地址

给定一个只包含数字的字符串，复原它并返回所有可能的IP地址格式

有效的IP地址正好由四个整数(每个整数位于0到255之间组成，且不能含有前导0),整数之间用'.'分隔

例如:
"0.1.2.201"和"192.168.1.1"是有效的IP地址，但是"0.011.255.245"、"192.168.1.312"和"192.168@1.1"是无效的IP地址

*/
#include <string>
#include <vector>
using namespace std;
class Solution {
private:
  vector<string> result;
  string str = "";
  void backtracking(string &s, int startIndex, int pointNum) {
    // 最简单的递归
    if (pointNum == 3) { // 说明分割完毕
      // 判断第四段是否合法
      if (isValid(s, startIndex, s.size() - 1)) {
        result.push_back(s);
      }
      return;
    }
    // 一般的逻辑
    for (int i = startIndex; i < s.size(); i++) {
      if (isValid(s, startIndex, i)) {
        //[startIndex,i]满足条件,就递归去分割
        s.insert(s.begin() + i + 1, '.'); // 在i的后面添加'.'
        pointNum++;
        backtracking(s, i + 2, pointNum);
        pointNum--;
        s.erase(s.begin() + i + 1);
      } else
        break; // 不合法，直接结束本层循环，因为01不合法，那01+都不会合法，减枝操作
    }
  }
  bool isValid(const string &s, int start, int end) {
    if (start > end) {
      return false;
    }
    if (s[start] == '0' && start != end) {
      // 0开头不合法
      return false;
    }
    int num = 0;
    for (int i = start; i <= end; i++) {
      if (s[i] > '9' || s[i] < '0') {
        // 非法数字
        return false;
      }
      num = num * 10 + (s[i] - '0');
      if (num > 255) {
        // 大于255 非法
        return false;
      }
    }
    return true;
  }

public:
  vector<string> restoreIpAddresses(string s) {
    result.clear();
    if (s.size() < 4 || s.size() > 12)
      return result;
    backtracking(s, 0, 0);
    return result;
  }
};
