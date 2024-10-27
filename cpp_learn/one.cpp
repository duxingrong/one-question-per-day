/*
A+B的问题 任务是计算A+B,这里需要能够循环输入a,b
，对于每对ab，你都需要一次输出他们的和
*/

#include <iostream>
int main() {
  int a, b;
  while (std::cin >> a >> b) {
    int result = a + b;
    std::cout << result << std::endl;
  }
  return 0;
}

// 可以在开头申明命名空间，就不用打std::
#include <iostream>
using namespace std;
int main() {
  int a, b;
  while (cin >> a >> b) {
    int result = a + b;
    cout << result << endl;
  }
  return 0;
}
