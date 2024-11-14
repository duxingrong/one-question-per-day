/*
判断一个数是不是快乐数

对于一个正整数,每一次将该数替换为它每个位置上的数字的平方和,然后重复这个过程知道这个数变成1,也可能是无限循环但始终变不到1。如果可以变成1,那么这个数就是快乐数

*/

#include <set>
class Solution {
public:
  int get_sum(int val) {
    int sum = 0;
    while (val) {
      int n = val % 10; // 获取最后一位
      val = val / 10;   // 删去最后一位
      sum += n * n;
    }
    return sum;
  }

  bool isHappy(int val) {
    std::set<int> nums;
    while (nums.find(val) == nums.end()) {
      if (val == 1) {
        return true;
      }
      nums.insert(val);
      val = get_sum(val);
    }
    return false;
  }
};
