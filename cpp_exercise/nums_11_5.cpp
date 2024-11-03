/*
给定一个整数数组Array,请计算该数组在每个指定区间内元素的总和

第一行输入为整数数组Array的长度n,接下来n行，每行一个整数,表示数组的元素，随后的输入为需要计算总和的区间(闭区间)，直至文件结束

输出每个指定区间内元素的总和
*/

#include <iostream>
#include <vector>

int main() {
  int n;
  std::cin >> n;
  std::vector<int> nums(n);
  std::vector<int> p(n);
  int sum = 0;
  for (int i = 0; i < n; i++) {
    int val;
    std::cin >> val;
    nums[i] = val;
    sum += val;
    p[i] = sum;
  }
  int a, b;
  while (std::cin >> a >> b) {
    int result;
    if (a == 0)
      result = p[b];
    else
      result = p[b] - p[a - 1];
    std::cout << result << std::endl;
  }
}
