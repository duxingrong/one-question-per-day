/*
在餐厅里，洗盘子的工作需要使用到栈这种数据结构
假设你手里有一个盘子堆放区，现在需要模拟洗盘子的过程，每个盘子都有一个编号
盘子堆放区操作说明:
1. 当操作为1时，表示从盘子堆放区拿走顶部的盘子清洗
2. 当操作为2时，表示有未洗的盘子放入盘子堆放区
在一系列操作之后，你需要回答:下一个清洗盘子的编号?

输入描述:
第一行有一个整数n,代表初始盘子堆放区中盘子的数量为n
第二行有n个整数，代表了盘子的编号，同时整数之间的顺序也代表了未洗盘子加入盘子堆放区的顺序
第三行为一个整数m，代表接下来将会有m次操作
如果是操作1,那么该行只会有一个数字1,代表有一个盘子被拿走清洗
如果是操作2,那么该行有两个数字，第一个数字2表示有未洗的盘子加入，第二个数字代表未洗的盘子的编号

输出共一行，为下一个该清洗的盘子编号，如果没有下一个该清洗的盘子，那么请输出"All
the dishes have been washed."
*/

#include <iostream>
#include <stack>
int main() {
  int n;
  std::cin >> n;
  std::stack<int> st;
  while (n--) {
    int data;
    std::cin >> data;
    st.push(data);
  }
  int m;
  std::cin >> m;
  while (m--) {
    int a;
    std::cin >> a;
    if (a == 1) {
      if (!st.empty()) {
        st.pop();
      }
    } else {
      int b;
      std::cin >> b;
      st.push(b);
    }
  }
  if (st.empty()) {
    std::cout << "All the dishes have been washed.";
  } else {
    int value = st.top();
    std::cout << value << std::endl;
  }
}
