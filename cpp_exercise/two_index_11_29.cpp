/*
移除元素
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val
的元素，并返回移除后数组的新长度
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
  int removeElement(vector<int> &nums, int val) {
    int left = 0;
    int right = nums.size() - 1;
    while (left < right) {
      while (left < right && nums[left] != val)
        left++;
      while (left < right && nums[right] == val)
        right--;
      // 交换时要确保left<right
      if (left < right) {
        swap(nums[left], nums[right]);
        left++;
        right--;
      }
    }
    // left==right时单独判断:
    if (left < nums.size() && nums[left] != val)
      left++;
    return left;
  }
};

int main() {
  vector<int> nums = {3, 3};
  int val = 3;
  Solution obj;
  int result = obj.removeElement(nums, val);
  cout << result << endl;
}
