/*

实现strStr()函数
给定一个haystack字符串和一个needle字符串，在haystack字符串中找出needle字符串出现的第一个位置(从0开始)，如果不存在，则返回-1

举例: haystack = "hello" ,needle="ll" 输出2

说明，当needle是空字符串的时候，我们应该返回什么值，返回0,与c语言的strstr()以及java的indexOf()定义相符


next[i]的定义:
next[i]表示从字符串的开头到索引i这部分子串(即s[0...i])中，最长相等的真前缀和真后缀的长度

如果s[i]==s[j]，说明后缀和前缀匹配成功，j会增加1,表示前后缀长度延长
如果s[i]!=s[j],说明匹配失败，我们通过next[j-1]，找到一个更短的前缀，再次尝试匹配，
直到j=0(没有更短的前缀可回退)

在kmp算法中，j始终指向模式串中当前匹配的最长前缀的下一个字符
当s[i] == s[j]:
s[j]: 是前缀的下一个字符
s[i]：是后缀的下一个字符
如果等于: 说明前缀和后缀的匹配长度扩展1,因此，我们增加j的值
*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;
class Solution {
public:
  void getNext(string &s, int *next) {
    next[0] = 0;
    int j = 0; // j指向前缀末尾
    for (int i = 1; i < s.size(); i++) {
      while (j > 0 && s[i] != s[j]) {
        j = next[j - 1];
      }
      if (s[i] == s[j]) {
        j++;
      }
      next[i] = j;
    }
  }

  int strStr(string &haystack, string &needle) {
    // 特殊情况
    if (needle.size() == 0)
      return 0;
    // 求模式串的next数组
    vector<int> next(needle.size());
    getNext(needle, &next[0]);
    int j = 0;
    for (int i = 0; i < haystack.size(); i++) {
      while (j > 0 && haystack[i] != needle[j]) {
        j = next[j - 1];
      }
      if (haystack[i] == needle[j]) {
        j++;
      }
      if (j == needle.size())
        return (i - needle.size() + 1);
    }
    return -1;
  }
};
