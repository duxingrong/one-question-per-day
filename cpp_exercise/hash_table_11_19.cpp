/*
给定一个赎金信(ransom)字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成,如果可以构成，返回true,否则返回false

为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次

你可以假设两个字符串均只有小写字母

canConstruct("aa","aab")->true
canConstruct("aa","ab")->false

这个题目就是对于数组哈希表的应用
*/

#include <string>
using namespace std;
class Solution {
public:
  bool canConstruct(string &ransom, string &magazine) {
    // 初始化哈希表
    int arr[26] = {0};
    // 如果ransom.size>magazine,直接false
    if (ransom.size() > magazine.size()) {
      return false;
    }
    //  遍历magazine，加入哈希表,记录字符的次数
    for (int i = 0; i < magazine.length(); i++) {
      arr[magazine[i] - 'a']++;
    }
    for (int i = 0; i < ransom.size(); i++) {
      arr[ransom[i] - 'a']--;
      if (arr[ransom[i] - 'a'] < 0) {
        return false;
      }
    }
    return true;
  }
};
