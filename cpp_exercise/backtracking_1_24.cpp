/*

组合总和||

给定一个数组candidates和一个目标数target,找出candidates中所有可以使数字和为target的组合.

candidates中每个数字在每个组合中只能使用一次。

说明: 所有数字(包括目标数)都是正整数。解集不能包含重复的组合。


去重，需要排序

*/

#include <algorithm>
#include <vector>
using namespace std;

class Solution {
private:
  vector<vector<int>> result;
  vector<int> path;
  void backtracking(vector<int> &candidates, int startIndex, int Sum,
                    int target) {
    //终止条件
    if (Sum > target) {
      return;
    }
    if (Sum == target) {
      result.push_back(path);
      return;
    }
    //一般递归处理
    for (int i = startIndex; i < candidates.size(); i++) {
      //去重
      if (i > startIndex && candidates[i] == candidates[i - 1]) {
        continue;
      }
      Sum += candidates[i];
      path.push_back(candidates[i]);
      backtracking(candidates, i + 1, Sum, target);
      Sum -= candidates[i];
      path.pop_back();
    }
  }

public:
  vector<vector<int>> combinationSum2(vector<int> candidates, int target) {
    path.clear();
    result.clear();
    //排序
    sort(candidates.begin(), candidates.end());
    backtracking(candidates, 0, 0, target);
    return result;
  }
};
