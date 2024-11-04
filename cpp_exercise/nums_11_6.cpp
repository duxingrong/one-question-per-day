/*
在一个城市区域内，被划分成了n*m个连续的区块,每个区块都拥有不用的权值，代表着土地价值，目前，有两家开发公司，A公司和B公司，希望购买这个城市区域的土地
现在，需要将这个城市区域的所有区块分配给A公司和B公司
然而，由于城市的限制，只允许将区域按横向或者纵向划分为两个子区域，为了确保公平竞争，你需要找到一种分配方式，使得A公司和B公司各自的子区域内的土地总价值之差最小

输入:
2 3
1 2 3
2 1 3
1 2 3

输出:
0

*/
#include <climits>
#include <iostream>
#include <vector>
int main() {
  int n, m;
  std::cin >> n >> m;
  std::vector<std::vector<int>> nums(n, std::vector<int>(m, 0));
  int data;
  int sum = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      std::cin >> data;
      nums[i][j] = data;
      sum += data;
    }
  }
  int result = INT_MAX;
  // 按照行来分割
  int count = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      count += nums[i][j];

      if (j == m - 1)
        result = std::min(result, abs(sum - count - count));
    }
  }
  // 按照列来分
  count = 0;
  for (int j = 0; j < m; j++) {
    for (int i = 0; i < n; i++) {
      count += nums[i][j];

      if (i == n - 1)
        result = std::min(result, abs(sum - count - count));
    }
  }
  std::cout << result << std::endl;
}
