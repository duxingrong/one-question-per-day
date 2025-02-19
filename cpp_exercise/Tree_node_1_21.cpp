/*

 数组总和|||

 找出所有相加之和为n的k个数的组合。组合中只允许含有1-9的正整数,并且每个组合中不存在重复的数字。

 说明:
 - 所有数字都是正整数
 - 解集不能包含重复的组合

 */
#include <vector>
using namespace std;
class Solution {
public:
  vector<vector<int>> combinationSum3(int k, int n) {
    result.clear();
    path.clear();
    backingtracking(0, n, k, 1);
    return result;
  }

private:
  vector<vector<int>> result;
  vector<int> path;
  void backingtracking(int Sum, int targetSum, int k, int startIndex) {
    if (Sum > targetSum) //剪枝
      return;

    if (path.size() == k) {
      //还要判断是否等于n
      if (Sum == targetSum) {
        result.push_back(path);
      }
      return;
    }

    for (int i = startIndex; i <= 9 - (k - path.size()) + 1; i++) {
      path.push_back(i);
      Sum += i;
      backingtracking(Sum, targetSum, k, i + 1);
      Sum -= i;
      path.pop_back();
    }
  }
};
