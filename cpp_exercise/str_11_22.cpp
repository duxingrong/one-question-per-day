/*

翻转字符串

编写一个函数，其作用是将输入的字符串反转过来,输入字符串以字符数组char[]的形式给出

不要给另外的数组分配额外的空间，你必须原地修改输入数组，使用O(1)的额外空间解决这一个问题

你可以假设数组中的所有字符都是ASCll码表中的可打印字符

 */

#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
  vector<char> reverseString(vector<char> &nums) {
    int left = 0;
    int right = nums.size() - 1;
    while (left < right) {
      char tmp;
      swap(nums[left], nums[right]);
      left++;
      right--;
    }
    return nums;
  }
};

int main() {
  vector<char> nums = {'a', 'b', 'c', 'd', 'e'};
  Solution obj;
  vector<char> reversenums = obj.reverseString(nums);
  for (const char num : reversenums) {
    cout << num << " ";
  }
}
