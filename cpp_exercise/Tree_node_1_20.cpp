/*
组合，优化剪枝

给定两个整数n和k，返回1...n中所有可能的k个数的组合

*/

#include <vector>
using namespace std;
class Solution {
private:
  vector<vector<int>> result;
  vector<int> path;
  void backtracking(int n, int k, int startIndex) {
    if (path.size() == k) {
      result.push_back(path);
      return;
    }
    for (int i = startIndex; i <= n - (k - path.size()) + 1; i++) {
      path.push_back(i);         //处理节点
      backtracking(n, k, i + 1); //递归
      path.pop_back();           //回溯
    }
  }

public:
  vector<vector<int>> combine(int n, int k) {
    result.clear();
    path.clear();
    backtracking(n, k, 1);
    return result;
  }
};
