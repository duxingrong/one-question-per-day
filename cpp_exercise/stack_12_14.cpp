/*
滑动窗口的最大值

给定一个数组nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧，你值可以看到在滑动窗口内的k的数字，滑动窗口每次只向右移动一位

返回滑动窗口中的最大值


nums = [1,3,-1,-3,5,3,6,7]
k = 3
输出: [3,3,5,5,6,7]
 */

/*
这个题目难点就在于我们要知道怎么维护我们的队列,这里巧妙的利用了单调递减队列
这样的话，我们可以实现每次que.front就是当前窗口的最大值
*/

#include <deque>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
  class MyQueue { // 单调队列，从大到小
  public:
    deque<int> que;
    // 每次弹出的时候，判断当前要弹出的值是否等于队列出口的值，等于才弹出，否则不管
    // 同时pop之前要判断是否为空
    void pop(int value) {
      if (!que.empty() && value == que.front()) {
        que.pop_front();
      }
    }

    // 入队列的时候要满足递减才行
    void push(int value) {
      while (!que.empty() && value > que.back()) {
        que.pop_back();
      }
      que.push_back(value);
    }

    // 当前队列的最大值，就是第一个值
    int front() { return que.front(); }
  };

public:
  vector<int> maxSlidingWindow(vector<int> &nums, int k) {
    MyQueue que;
    vector<int> result;
    for (int i = 0; i < k; i++) {
      que.push(nums[i]);
    }
    result.push_back(que.front());
    // 开始移动窗口
    for (int i = k; i < nums.size(); i++) {
      que.pop(nums[i - k]);
      que.push(nums[i]);
      result.push_back(que.front());
    }
    return result;
  }
};

int main() {
  vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
  int k = 3;
  Solution obj;
  vector<int> result = obj.maxSlidingWindow(nums, k);
  for (const int val : result) {
    cout << val << " "; // 输出: [3,3,5,5,6,7]
  }
}
