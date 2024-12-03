/*
翻转字符串里的单词

给定一个字符串，逐个翻转字符串中的每个单词
"the sky is blue"
"blue is sky the"
*/

#include <algorithm>
#include <sstream>
#include <string>

using namespace std;
class Solution {
public:
  string reverseWords(string &s) {
    // 将字符串变成输入流
    istringstream iss(s);
    vector<string> words;
    string word;
    while (iss >> word) {
      words.push_back(word);
    }
    reverse(words.begin(), words.end());
    string result;
    for (int i = 0; i < words.size(); i++) {
      result += words[i];
      if (i != words.size() - 1) {
        result += " ";
      }
    }
    return result;
  }
};
