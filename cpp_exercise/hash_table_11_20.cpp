/*
三数之和
给你一个包含n个整数的数组nums,判断nums中是否存在三个元素a,b,c,使得a+b+c=0?请你找出所有满足条件且不重复的三元组
注意: 答案中不可以包含重复的三元组

示例：
给定数组 nums=[-1,0,1,2,-1,-4]
满足要求的三元组集合为: [[-1,0,1],[-1,-1,2]]


这个题目用的是双指针，怎么说呢，我们用i,left,right来遍历三个数，满足=0就加入
但是要知道怎么对a,b,c进行去重
 */
#include <algorithm> //排序
#include <vector>
using namespace std;
class Solution {
public:
  vector<vector<int>> threeSum(vector<int> &nums) {
    // 排序
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    for (int i = 0; i < nums.size() - 2; i++) {
      // 去重a
      if (i > 0 && nums[i] == nums[i - 1])
        continue;
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
          // 对b 和c去重
          while (left < right && nums[left] == nums[left + 1])
            left++;
          while (left < right && nums[right] == nums[right - 1])
            right--;

          // 结果有了后。都需要加1
          left++;
          right--;
        }
      }
    }
    return result;
  }
};
