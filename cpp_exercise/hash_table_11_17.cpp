/*
给定一个整数数组nums和一个目标值target,请你在该数组中找出和为目标的那两个整数，并返回他们的数组下标

你可以假设每种输入只会对应一个答案,但是，数组中同一个元素不嫩使用两遍

实例:
给定nums=[2, 7,11,15] , target = 9
因为nums[0]+nums[1]=2+7=9
返回[0,1]

 */
#include <unordered_map>
#include <vector>
using namespace std;
class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    unordered_map<int, int> map;
    for (int i = 0; i < nums.size(); i++) {
      auto iter = map.find(target - nums[i]);
      if (iter != map.end()) {
        return {iter->second, i};
      } else {
        map.insert(pair<int, int>(nums[i], i));
      }
    }
    return {};
  }
};
