/*

输入包含多组测试样例，每组测试样例包含一个正整数n，表示小明已经堆好的积木堆的个数
接着下一行是n个正整数，表示每一个积木堆的高度h，每块积木高度为1，测试数据保证积木总数能被积木堆整数整除
当n=0时候，输入结束


对于每一组数据，输出将积木堆变成相同高度需要移动的最少积木块的数量。在每组输出结果的下面都需要输出一个空行

输入:
6
5 2 4 1 7 5
0

输出:
5


如个计算最少的步骤?
每一个nums[i]-平均值取绝对值，然后/2

*/

#include <iostream>
#include <vector>
int main() {
  int n, m;
  while (std::cin >> n) {
    if (n == 0)
      break;
    int sum = 0;
    std::vector<int> nums;
    for (int i = 0; i < n; i++) {
      std::cin >> m;
      nums.push_back(m);
      sum += m;
    }
    int target = sum / n;
    int ans = 0;
    for (int i = 0; i < n; i++) {
      ans += abs(nums[i] - target);
    }
    ans = ans / 2;
    std::cout << ans << std::endl; // 输出结果并将光标放到下一行
    std::cout << std::endl;        // 所以需要这里再次换行，分隔结果
  }
}
