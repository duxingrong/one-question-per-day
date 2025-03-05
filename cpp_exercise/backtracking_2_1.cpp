/*
重新安排行程

给定一个机票的字符串二维数组[from,to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划和排序。所有这些机票都属于一个从JFK(肯尼迪国际机场)出发的先生，所以该形成必须从JFK开始。


如果存在多种有效的行程，请你按字符自然排序返回最小的行程组合

*/
#include <map>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
private:
  //这里是用map来实现自然排序
  //创建结构unorder_map<出发机场,map<到达机场,航班次数>> targets
  unordered_map<string, map<string, int>> targets;
  // 这里返回值为bool是因为只要找到了就可以了
  // result 就是结果列表 ， ticketNum 就是机票的数量，ticketNum+1就是机场的总数
  bool backtracking(vector<string> &result, int ticketNum) {
    //终止条件
    if (result.size() ==
        ticketNum + 1) { //相当所有的机场都加入了结果集，返回true
      return true;
    }
    //一般的逻辑
    for (pair<const string, int> &target : targets[result[result.size() - 1]]) {
      //如果还有机票，就起飞
      if (target.second > 0) {
        result.push_back(target.first);
        target.second--;
        if (backtracking(result, ticketNum)) {
          return true;
        }
        result.pop_back();
        target.second++;
      }
    }
    return false;
  }

public:
  vector<string> findItinerary(vector<vector<string>> &tickets) {
    targets.clear();
    vector<string> result;
    for (const vector<string> &vec : tickets) {
      targets[vec[0]][vec[1]]++; //记录映射关系
    }
    result.push_back("JFK"); //起始机场
    backtracking(result, tickets.size());
    return result;
  }
};
