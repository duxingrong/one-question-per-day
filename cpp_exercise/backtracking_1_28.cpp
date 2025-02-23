/*
子集||

给定一个可能包含重复元素的整数数组nums,返回该数组所有可能的子集(幂集)

说明:解集不能包含重复的子集

输入:[1,2,2]
输出:[[2],[1],[1,2],[2,2],[1,2],[]]

*/
#include <algorithm>
#include <vector>
using namespace std;
class Solution {
private:
  vector<vector<int>> result;
  vector<int> path;
  void backtracking(vector<int> &nums, int startIndex) {
    // 每一次进入都需要先记录
    result.push_back(path);

    // 最简单的逻辑,可以省略，因为超过了不会执行for循环，自动退出
    if (startIndex >= nums.size()) {
      return;
    }

    // 一般的逻辑
    for (int i = startIndex; i < nums.size(); i++) {
      // 去重
      if (i > startIndex && nums[i] == nums[i - 1]) {
        continue;
      }
      path.push_back(nums[i]);
      backtracking(nums, i + 1);
      path.pop_back(); // 回溯
    }
  }

public:
  vector<vector<int>> subsetsWithDup(vector<int> nums) {
    result.clear();
    path.clear();
    sort(nums.begin(), nums.end());
    backtracking(nums, 0);
    return result;
  }
};
