/*
翻转字符串里的单词

给定一个字符串，逐个反转字符串中的每个单词
"the sky is blue"
"blue is sky the"

 */
#include <algorithm> //reverse
#include <iostream>
#include <sstream> //istringstream
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
  string reverseWords(string &s) {
    // 如何以空格分割字符串
    istringstream iss(s); // 将s变成输入流,这样>>时候会自动以空格分开
    vector<string> words;
    string word;
    // 进入数组
    while (iss >> word) {
      words.push_back(word);
    }
    // 反转数组
    reverse(words.begin(), words.end());
    // 输出结果
    string result;
    for (int i = 0; i < words.size(); i++) {
      result += words[i];
      if (i != words.size() - 1)
        result += " ";
    }
    return result;
  }
};

int main() {
  string s = "the sky is blue";
  Solution obj;
  string result = obj.reverseWords(s);
  cout << result << endl;
}
