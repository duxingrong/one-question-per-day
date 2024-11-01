/*
给定一个含有n个正整数的数组和一个正整数s，找出该数族中满足其和>=s的长度最小的连续子数组，并返回其长度，如果不存在符合条件的子数组，返回0.

输入: s=7 nums= [2,3,1,2,4,3]
输出2
[4,3] 最小长度为2

考察滑动窗口
窗口内的元素是其和>=s的长度最小的连续子数组
*/
#include <climits>
#include <iostream>
#include <vector>
class Solution {
public:
  int minSubArrayLen(const int s, std::vector<int> &nums) {
    // 创建窗口
    int left = 0;
    int right = 0;
    int result = INT_MAX;
    int sum = 0;
    while (right < nums.size()) {
      // 窗口要不断扩大
      sum += nums[right];
      right += 1;
      while (sum >= s) // 直到大于s的时候
      {
        result = std::min(result, right - left); // 记录最小长度
        sum -= nums[left];
        left += 1;
      }
    }
    return result == INT_MAX ? 0 : result;
  };
};

int main() {
  std::vector<int> nums = {2, 3, 1, 2, 4, 3, 7};
  int s = 7;
  Solution solution;
  int ans = solution.minSubArrayLen(s, nums);
  std::cout << ans << std::endl;
}
