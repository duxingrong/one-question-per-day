/*
删除字符串中的所有相邻重复项

给出由小写字符组成的字符串S,重复项删除操作会选择两个相邻且相同的字母，并删除它们
在S上反复执行重复项删除操作，直到无法继续删除
在完成所有重复项删除操作后返回最终的字符串，答案保证唯一

例如："abbaca" 
输出 ： "ca"
*/


//典型的用栈操作即可
#include <stack>
#include <string>
#include <algorithm>
using namespace std;
class Solution{
public:
    string removeDuplicates(string S){
        stack<char> st ;
        for (int i = 0 ; i<S.size();i++ ){
            if (!st.empty() && S[i]==st.top()){
                st.pop();
            }else {
                st.push(S[i]);
            }
        }
        //将剩余的st中的元素取出来
        string result ="";
        while (!st.empty()){
            result+=st.top();
            st.pop();
        }
        reverse(result.begin() , result.end());
        return result;
    }
};