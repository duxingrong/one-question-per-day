/*

有效的括号

给定一个只包括'(',')','{','}'，'[',']'的字符串，判断字符串是否有效

有效字符串需满足:

- 左括号必须用相同类型的右括号闭合.
- 左括号必须以正确的顺序闭合.
- 注意空字符串可被认为是有效字符串

()[]{} true
([)]   false

 */

#include <stack>
#include <string>
#include <vector>
using namespace std;
class Solution {

public:
  bool isValid(string s) {
    // 创建栈
    stack<char> st;
    // 如果长度为奇数，直接false
    if (s.size() % 2 != 0)
      return false;
    for (int i = 0; i < s.size(); i++) {
      if (s[i] == '(')
        st.push(')');
      else if (s[i] == '[')
        st.push(']');
      else if (s[i] == '{')
        st.push('}');
      // 其他的情况，就需要判断是否出错
      else if (st.empty() || s[i] != st.top())
        // 直接栈空了，你输入却是反括号，直接pass,或者你的括号无法抵消，那也是错了
        return false;
      else
        st.pop();
    }
    return st.empty(); // 遍历完成后，如果不为空，说明前括号没有抵消，错误
  }
};
