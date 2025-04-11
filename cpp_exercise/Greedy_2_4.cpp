#include <algorithm>
#include <vector>
using namespace std;
/**
 * @brief 分发饼干
 */

class Solution {
public:
  /**
   * @brief 贪心算法，每次让小饼干满足胃口小的人
   *
   * @param g 小孩的胃口
   * @param s 饼干的大小
   *
   * @return gIndex 满足小孩的个数
   */
  int findContentChildren(vector<int> &g, vector<int> &s) {
    sort(s.begin(), s.end());
    sort(g.begin(), g.end());
    int gIndex = 0;
    for (size_t i = 0; i < s.size(); ++i) {
      if (gIndex < g.size() && s[i] >= g[gIndex]) {
        gIndex++;
      }
    }
    return gIndex;
  }
};
