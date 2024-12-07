/*

三数之和

给你一个包含n个整数的数组nums,判断nums中是否存在三个元素a,b,c,使得a+b+c = 0?
请你找出所有满足条件且不重复的三元组

答案中不可以包含重复的三元组

 */

// a 的去重 ，在for 循环的时候去重
// ，b和c是双指针，所以去重用while来去重(当收获到结果的时候)

#include <algorithm>
#include <vector>
using namespace std;
class Solution {
public:
  vector<vector<int>> threeSum(vector<int> &nums) {
    // 排序
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    for (int i = 0; i < nums.size() - 2; i++) {
      // 减枝
      if (nums[i] > 0) {
        break;
      }
      //  a去重
      if (i > 0 && nums[i] == nums[i - 1]) {
        continue;
      }
      int left = i + 1;
      int right = nums.size() - 1;
      while (left < right) {
        int sum = nums[i] + nums[left] + nums[right];
        if (sum > 0) {
          right--;
        } else if (sum < 0) {
          left++;
        } else {
          result.push_back({nums[i], nums[left], nums[right]});
          left++;
          right--;
          // 对b,c去重
          while (left < right && nums[left] == nums[left - 1])
            left++;
          while (left < right && nums[right] == nums[right + 1])
            right--;
        }
      }
    }
    return result;
  }
};
