/*
给你一个按非递减顺序排序的整数数组nums，返回每个数字的平方组成的新数组，要求也按非递减顺序排序


双指针，加上一个新数组的指针
left=0;
right=nums.size()-1;
index = nums.size()-1;
std::vector<int> result;
比较出最大者加入到结果集里面
*/

#include <iostream>
#include <vector>
class Solution {
public:
  std::vector<int> sortedSquares(const std::vector<int> nums) {
    // 设置指针和数组
    int left = 0;
    int right = nums.size() - 1;
    std::vector<int> result(nums.size());
    int index = result.size() - 1;
    while (left <= right) {
      if (nums[left] * nums[left] >= nums[right] * nums[right]) {
        result[index] = nums[left] * nums[left];
        index -= 1;
        left += 1;
      } else {
        result[index] = nums[right] * nums[right];
        index -= 1;
        right -= 1;
      }
    }
    return result;
  };
};

int main() {
  std::vector<int> nums = {-4, -1, 0, 3, 10};
  Solution obj;
  nums = obj.sortedSquares(nums);
  // 打印数组
  for (int num : nums) {
    std::cout << num << " ";
  }
  std::cout << std::endl;
  return 0;
}
