/*
给定一个n个元素有序的(升序)整型数组nums和一个目标值target,写一个函数搜索nums中的target,如果目标值存在返回下标，否则返回-1
*/

#include <iostream>
#include <vector>
class Solution {
public:
  // 二分查找的函数
  int search(const std::vector<int> &nums, int target) {
    int left = 0;
    int right = nums.size() - 1;
    while (left <=
           right) { // 这里极端一点，假设只有一个值，那要找到肯定只能left=right
      int index = (left + right) / 2;
      if (nums[index] > target) { // 中间值大于目标值
        right = index - 1;
      } else if (nums[index] < target) { // 中间值小于目标值
        left = index + 1;
      } else {
        return index;
      }
    }
    return -1;
  };
};

int main() {
  std::vector<int> nums = {1, 2, 3, 4, 5};
  int target = 3;
  Solution obj;
  int result = obj.search(nums, target);
  std::cout << result << std::endl;
}
// 二分法只要注意等好的条件，left<=right
