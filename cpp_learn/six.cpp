/*
给定一个数组，编写一个程序实现以下功能:
1. 将输入的整数数组倒序输出，每个数之间用空格分隔
2. 从正序数组中，每隔一个单位(即索引为奇数的元素)，输出其值，同样用空格分隔


第一行包含一个整数n，表示数组的长度。接下来一行包含n个整数，表示数组的元素

首先输出倒序排列的数组元素，然后输出正序数组中每隔一个单位的元素

*/

// 使用vector
#include <iostream>
#include <vector>
int main() {
  int n, m;
  std::cin >> n;
  // 这里创建数组
  std::vector<int> nums;
  while (n--) {
    std::cin >> m;
    nums.push_back(m);
  }
  // 倒序输出
  for (int i = nums.size() - 1; i >= 0; i--) {
    std::cout << nums[i];
    if (i > 0)
      std::cout << " ";
  }
  std::cout << std::endl;
  for (int i = 0; i < nums.size(); i += 2) {
    std::cout << nums[i];
    if (i < nums.size() - 1)
      std::cout << " ";
  }
  return 0;
}

// 使用数组
#include <iostream>
int main() {
  int n, m;
  std::cin >> n;
  int arr[n];
  for (int i = 0; i < n; i++) {
    std::cin >> m;
    arr[i] = m;
  }
  // 到序输出
  for (int i = n - 1; i >= 0; i--) {
    std::cout << arr[i] << " ";
  }
  std::cout << std::endl;
  // 隔位输出
  for (int i = 0; i < n; i += 2) {
    std::cout << arr[i] << " ";
  }
  return 0;
}
