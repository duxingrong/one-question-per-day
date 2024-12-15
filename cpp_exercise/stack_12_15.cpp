/*

前k个高频元素

给定一个非空的整数数组，返回其中出现频率前k高的元素

nums = [1,1,1,2,2,3] k =2

输出[1,2]

 */

// 如何记录出现的频率
// 如何排序
// priority_queue<Type,Container,Compare>
// #用于实现大顶堆，可以自定义比较器实现小顶堆
// Type:存储的元素类型 Container:底层容器，通常是vector或者deque  Compare:比较器

#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
  // 自定义比较器
  class mycomparison {
  public:
    bool operator()(const pair<int, int> &lhs, const pair<int, int> &rhs) {
      return lhs.second > rhs.second;
    }
  };

  // 主函数
  vector<int> topKFrequent(vector<int> &nums, int k) {

    // 首先用map记录频率
    unordered_map<int, int> map;
    for (int i = 0; i < nums.size(); i++) {
      map[nums[i]]++;
    }

    // 利用小顶堆排序
    priority_queue<pair<int, int>, vector<pair<int, int>>, mycomparison>
        pri_que;

    // 遍历map
    for (unordered_map<int, int>::iterator it = map.begin(); it != map.end();
         it++) {
      pri_que.push(*it); //*it是用来解引用迭代器it,获取它所指向的元素
      // 堆只维护k个元素
      if (pri_que.size() > k) {
        pri_que.pop();
      }
    }

    // 将堆中元素传给数组返回
    vector<int> result(k);
    for (int i = k - 1; i > -1; i--) {
      result[i] = pri_que.top().first;
      pri_que.pop();
    }
    return result;
  }
};
