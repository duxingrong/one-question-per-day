/*

组合

给定两个整数n和k，返回1...n中所有可能的k个数的组合。

示例:输入:n=4,k=2,输出:[[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]

*/
#include <vector>
using namespace std;
class Solution {
public:
  vector<vector<int>> combine(int n, int k) {
    result.clear();
    path.clear();
    backingtracking(n, k, 1);
    return result;
  }

private:
  vector<vector<int>> result; //存放符合条件结果的集合
  vector<int> path;           //用来存放符合条件结果
  void backingtracking(int n, int k, int startIndex) {
    if (path.size() == k) {
      result.push_back(path);
      return;
    }
    for (int i = startIndex; i <= n; i++) {
      path.push_back(i);            //处理节点
      backingtracking(n, k, i + 1); //递归
      path.pop_back();              //回溯，撤销处理的节点
    }
  }
};
