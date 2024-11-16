/*
给定四个包含整数的数组列表A，B，C，D，计算有多少个元组(i,j,k,l)，使得A[i]+B[j]+C[k]+D[j]=0

这个题目就是用map记录a+b的所有值的所有次数,然后遍历c+d,如果出现a+b+c+d=0,则count+=map(0-(c+d))
 */

#include <unordered_map>
#include <vector>
using namespace std;
class Solution {
public:
  int fourSumCount(vector<int> &A, vector<int> &B, vector<int> &C,
                   vector<int> &D) {
    unordered_map<int, int> umap;
    for (int a : A) {
      for (int b : B) {
        umap[a + b]++;
      }
    }

    int count = 0;
    for (int c : C) {
      for (int d : D) {
        if (umap.find(0 - (c + d)) != umap.end()) { // 说明找到了四数之和等于0
          count += umap[0 - (c + d)];
        }
      }
    }
    return count;
  }
};
