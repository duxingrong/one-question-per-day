#include <vector>
using namespace std;

/**
 * @brief 摆动序列
 */
class Solution {
public:
  /**
   * @param nums 给定的数组
   *
   * @return 最长摆动序列的长度
   */
  int wiggleMaxLength(vector<int> &nums) {
    int up = 1;
    int low = 1;
    for (size_t i = 1; i < nums.size(); ++i) {
      if (nums[i] > nums[i - 1])
        low = up + 1;
      else if (nums[i] < nums[i - 1])
        up = low + 1;
    }
    return max(low, up);
  }
};
