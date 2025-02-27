/*

全排列||

给定一个可包含重复数字的序列nums,按任意顺序返回所有不重复的全排列。

输入: nums=[1,1,2]
输出:[ [1,1,2],[1,2,1],[2,1,1]]


去重并且可以排序
*/
#include <algorithm>
#include <vector>
using namespace std;
class Solution {
private:
  vector<vector<int>> result;
  vector<int> path;
  void backtracking(vector<int> &nums, vector<bool> &used) {
    //终止条件
    if (path.size() == nums.size()) {
      result.push_back(path);
      return;
    }

    //一般的递归
    for (int i = 0; i < nums.size(); i++) {
      //如果该索引用过了，就跳过
      if (used[i] == true)
        continue;
      //要去重，如果这一层后面和前面数字一样,就要跳过
      // used[i-1]==true,说明同一树枝nums[i-1]使用过
      // used[i-1]==false,说明同一树层nums[i-1]使用过
      if (i > 0 && nums[i] == nums[i - 1] && used[i - 1] == false) {
        continue;
      }
      used[i] = true;
      path.push_back(nums[i]);
      backtracking(nums, used);
      path.pop_back();
      used[i] = false;
    }
  }

public:
  vector<vector<int>> permuteUnique(vector<int> &nums) {
    vector<bool> used(nums.size(), false);
    result.clear();
    path.clear();
    sort(nums.begin(), nums.end());
    backtracking(nums, used);
    return result;
  }
};
