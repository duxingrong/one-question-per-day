/*

给定一个没有重复数字的序列，返回其所有可能的全排列


排列就不是用startIndex ,而是用used 数组
*/
#include <vector>
using namespace std;
class Solution {
private:
  vector<vector<int>> result;
  vector<int> path;
  void backtracking(vector<int> &nums, vector<bool> &used) {
    // 最简单的逻辑
    if (path.size() == nums.size()) {
      result.push_back(path);
      return;
    }
    for (int i = 0; i < nums.size(); i++) {
      // 如果已经选过，就pass
      if (used[i] == true)
        continue;
      used[i] = true;
      path.push_back(nums[i]);
      backtracking(nums, used);
      path.pop_back();
      used[i] = false;
    }
  }

public:
  vector<vector<int>> permute(vector<int> &nums) {
    result.clear();
    path.clear();
    vector<bool> used(nums.size(), false);
    backtracking(nums, used);
    return result;
  }
};
