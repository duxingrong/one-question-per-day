/*
给定一个正整数n，生成一个包含1到n^2
所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵

输入3
输出[ [1,2,3],[8,9,4],[7,6,5]]
*/
#include <iostream>
#include <vector>
class Solution {
public:
  std::vector<std::vector<int>> generateMatrix(const int n) {
    std::vector<std::vector<int>> nums(n, std::vector<int>(n, 0));
    int count = 1;
    if (n % 2 == 1) {
      nums[n / 2][n / 2] = n * n; // 填充中间的值
    }
    for (int i = 0; i < n / 2; i++) {
      // 水平向右的边
      for (int j = i; j < n - 1 - i; j++) {
        nums[i][j] = count;
        count++;
      }
      // 竖直向下的边
      for (int j = i; j < n - 1 - i; j++) {
        nums[j][n - 1 - i] = count;
        count++;
      }
      // 水品向左的边
      for (int j = n - 1 - i; j > i; j--) {
        nums[n - 1 - i][j] = count;
        count++;
      }
      for (int j = n - 1 - i; j > i; j--) {
        nums[j][i] = count;
        count++;
      }
    }
    return nums;
  };
};

int main() {
  int n = 4;
  Solution solution;
  std::vector<std::vector<int>> result = solution.generateMatrix(n);
  for (const std::vector num : result) {
    for (const int val : num) {
      std::cout << val << " ";
    }
    std::cout << std::endl;
  }
}
