#include <climits>
#include <iostream>
#include <vector>
using namespace std;
/**
 * @brief 最大自序列
 */
class Solution {
public:
  /**
   * @brief 贪心，如果前面的是累赘，就丢掉他
   */
  int maxSubArray(vector<int> &nums) {
    int result = INT_MIN;
    int sum = 0;
    for (auto num : nums) {
      sum = max(sum + num, num);
      result = max(result, sum);
    }
    return result;
  }
};

int main() {
  Solution obj;
  vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
  auto result = obj.maxSubArray(nums);
  cout << result << endl;
}
