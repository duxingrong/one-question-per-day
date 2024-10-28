/*
你的任务时计算若干个整数的和
每行的第一个数N，表示本行后面有N个数。如果N=0时，表示输入结束，且这一行不要计算
对于每一行数据需要在相应的行输出和

4 1 2 3 4
5 1 2 3 4 5
0

输出:
10
15



这里唯一需要注意的是，while(std::cin>>N)他返回的是std::iostream对象的引用，他在流操作成功时会转换成true,只要输入是有效的(即使输入的值是0)，std::cin的状态是良好的，他的返回值会被视为true，并进入循环体

这里就是为什么需要if 来判断，为了及时跳出循环体
*/

#include <iostream>
int main() {
  int N;
  while (std::cin >> N) {
    if (N == 0)
      break;
    int sum = 0;
    int a = 0;
    while (N--) {
      std::cin >> a;
      sum += a;
    }
    std::cout << sum << std::endl;
  }
  return 0;
}
