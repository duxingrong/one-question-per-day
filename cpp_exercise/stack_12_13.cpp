/*

逆波兰表达式求值

根据逆波兰表示法，求表达式的值
有效的元算符包括+ , - , * , /
.每个运算对象可以是整数，也可以是另一个逆波兰表达式

整数除法只保留整数部分，给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为0的情况


输入: ['2','1','+','3',"*"]
输出： (2+1)*3 = 9

输入：['4','13','5',"/",'+']
输出： 4+(13/5) = 6

 */
#include <stack>
#include <string>
#include <vector>
using namespace std;
class Solution {
public:
  int evalRPN(vector<string> nums) {
    stack<long long> st;
    for (int i = 0; i < nums.size(); i++) {
      // 如果是数字，直接存入
      if (nums[i] == "+" || nums[i] == "-" || nums[i] == "*" ||
          nums[i] == "/") {
        long long b = st.top();
        st.pop();
        long long a = st.top();
        st.pop();
        if (nums[i] == "+")
          st.push(a + b);
        else if (nums[i] == "-")
          st.push(a - b);
        else if (nums[i] == "*")
          st.push(a * b);
        else if (nums[i] == "/")
          st.push(a / b);
      } else {
        st.push(stoll(nums[i]));
      }
    }
    int res = st.top();
    return res;
  }
};
