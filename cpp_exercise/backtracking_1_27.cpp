/*
子集

给定一组不含重复元素的整数数组nums,返回该数组所有可能的子集(幂集)

说明:解集不能包含重复的子集

输入:nums=[1,2,3]输出:[[3],[2],[1],[1,2,3],[1,3],[2,3],[1,2],[]]

*/

#include <vector>
using namespace std;
class Solution {
private:
  vector<vector<int>> result;
  vector<int> path;
  void backtracking(vector<int> nums, int startIndex) {
    // 每次进入递归，都要收集,相当于每个节点都要收集，以往是只收集叶子节点
    result.push_back(path);
    // 最简单的递归
    if (startIndex == nums.size()) {
      return;
    }
    // 一般的逻辑
    for (int i = startIndex; i < nums.size(); i++) {
      path.push_back(nums[i]);
      backtracking(nums, i + 1);
      path.pop_back();
    }
  }

public:
  vector<vector<int>> subsets(vector<int> &nums) {
    result.clear();
    path.clear();
    backtracking(nums, 0);
    return result;
  }
};
