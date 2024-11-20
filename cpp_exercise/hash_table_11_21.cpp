/*

四数之和
给定一个包含n个整数的数组nums和一个目标值target,判断nums中是否存在四个元素a,b,c和d,使得a+b+c+d的值与target相等？找出所有满足条件且不重复的四元组

例子:
nums=[1,0,-1,0,-2,2]，和target=0,
满足要求的四元组集合为:
[-1,0,0,1],[-2,-1,1,2],[-2,0,0,2]

 */

// 套娃
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
  vector<vector<int>> fourSum(vector<int> &nums, int target) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    for (int i = 0; i < nums.size(); i++) {
      // 剪枝
      if (nums[i] > target && nums[i] >= 0) {
        break;
      }
      // 去重
      if (i > 0 && nums[i] == nums[i - 1]) {
        continue;
      }
      for (int j = i + 1; j < nums.size(); j++) {
        if (nums[j] + nums[i] > target && nums[j] + nums[i] >= 0) {
          break;
        }
        if (j > i + 1 && nums[j] == nums[j - 1]) {
          continue;
        }

        int left = j + 1;
        int right = nums.size() - 1;
        while (left < right) {
          long long sum =
              (long long)nums[i] + nums[j] + nums[left] + nums[right];
          if (sum > target) {
            right--;
          } else if (sum < target) {
            left++;
          } else {
            result.push_back(
                vector<int>{nums[i], nums[j], nums[left], nums[right]});
            left++;
            right--;
            // c,d 去重
            while (left < right && nums[left] == nums[left - 1])
              left++;
            while (left < right && nums[right] == nums[right + 1])
              right--;
          }
        }
      }
    }
    return result;
  }
};
