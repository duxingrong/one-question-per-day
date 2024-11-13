/*
给定两个数组，编写一个函数来计算它们的交集
输出结果中的每个元素一定是唯一的，我们可以不考虑输出结果俄顺序

输入: [4,9,5] [9,4,9,8,4]
输出：[9,4]

这里利用unordered_set来去重和查找

*/
#include <unordered_set>
#include <vector>
using namespace std;
class Solution {
public:
  std::vector<int> intersection(std::vector<int> nums1,
                                std::vector<int> nums2) {
    std::unordered_set<int> result; // 设置一个unordered_set
    std::unordered_set<int> nums_set(nums1.begin(), nums1.end()); // 数组去重
    for (int num : nums2) {
      if (nums_set.find(num) !=
          nums_set.end()) { // 如果在nums_set中， 那find的返回就不会等于.end()
        result.insert(num);
      }
    }
    return std::vector<int>(result.begin(), result.end()); // 将set变成数组
  }
};
