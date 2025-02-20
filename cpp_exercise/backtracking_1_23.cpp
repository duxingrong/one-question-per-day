/*

组合总和

给定一个无重复元素的数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。

candidates中的数字可以无限制重复被选取

说明：
- 所有数字(包括target)都是正整数。
- 解集不能包含重复的组合。

*/

#include <vector>
using namespace std;
class Solution {
private:
  vector<vector<int>> result;
  vector<int> path;
  void backtracking(vector<int> &candidates, int Sum, int target,
                    int startIndex) {
    if (Sum > target) {
      return;
    }
    // 终止条件
    if (Sum == target) {
      result.push_back(path);
      return;
    }
    //一般的递归逻辑
    for (int i = startIndex; i < candidates.size(); i++) {
      Sum += candidates[i];
      path.push_back(candidates[i]);
      backtracking(candidates, Sum, target, i);
      Sum -= candidates[i];
      path.pop_back();
    }
  }

public:
  vector<vector<int>> combinationSum(vector<int> &candidates, int target) {
    result.clear();
    path.clear();
    backtracking(candidates, 0, target, 0);
    return result;
  }
};
