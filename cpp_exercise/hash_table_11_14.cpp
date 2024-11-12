/*
给定两个字符串s和t，编写一个函数来判断t是否是s的字母异位词
举例:
输入: s=anagram   t= nagaram
输出: true
你可以假设字符串只包含小写字母

经典的哈希表
*/
#include <iostream>
#include <string>
class Solution {
public:
  bool isAnagram(const std::string s, std::string t) {
    int arr[26] = {0};
    for (int i = 0; i < s.size(); i++) {
      arr[s[i] - 'a'] += 1;
    }
    for (int i = 0; i < t.size(); i++) {
      arr[t[i] - 'a'] -= 1;
    }

    for (int i = 0; i < 26; i++) {
      if (arr[i] != 0)
        return false;
    }
    return true;
  }
};

int main() {
  std::string s = "anagram";
  std::string t = "nagaram";
  Solution obj;
  bool result = obj.isAnagram(s, t);
  std::cout << (result ? "true" : "false") << std::endl;
}
