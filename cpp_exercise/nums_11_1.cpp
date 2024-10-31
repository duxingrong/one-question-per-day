/*
给你一个数组nums和一个值val,需要原地移除所有数值等于val的元素,并返回移除后数组的新长度

不要使用额外的数组空间，你必须使用O(1)额外空间并原地修改输入数组

元素的顺序可以改变，你不需要考虑数组中超出新长度后面的元素

双指针
while (left<=right)
if (left==val);
left+=1;
if (right!=val);
right-=1
else if (right==val and left!= val)
交换left 和right 的元素
然后left+=1; right-=1;

*/

#include <vector>
class Solution {
public:
  int removeElement(std::vector<int> &nums, int val) {
    // 双指针
    int left = 0;
    int right = nums.size() - 1;
    while (left <= right) {
      while (left <= right && nums[left] != val)
        left += 1;
      while (left <= right && nums[right] == val)
        right -= 1;
      if (left < right) {
        std::swap(nums[left], nums[right]); // 交换左右值
      }
    }
    return left; // 为什么是left，因为每次只要发现不等于val的值,left都会+1,left从0开始，加了几次就说明有几个数
  }
};
