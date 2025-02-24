/*
递增子序列

给定一个整形数组，你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2.


*/
#include <unordered_set>
#include <vector>
using namespace std;
class Solution {
private:
  vector<vector<int>> result;
  vector<int> path;
  void backtracking(vector<int> &nums, int startIndex) {
    // 最简单的逻辑
    // 如果长度大于=2,就加入
    // 不要return ,因为要继续遍历递增,根据startIndex的大小会自动退出
    if (path.size() >= 2) {
      result.push_back(path);
    }

    unordered_set<int> uset; // 使用set对本层元素去重
    for (int i = startIndex; i < nums.size(); i++) {
      if (uset.find(nums[i]) != uset.end() ||
          path.size() != 0 && nums[i] < path.back()) {
        continue; // 去重，以及如果不是递增也要跳过
      }
      uset.insert(nums[i]); // 在本层使用过了
      path.push_back(nums[i]);
      backtracking(nums, i + 1);
      path.pop_back();
    }
  }

public:
  vector<vector<int>> findSubsequences(vector<int> &nums) {
    result.clear();
    path.clear();
    backtracking(nums, 0);
    return result;
  }
};
