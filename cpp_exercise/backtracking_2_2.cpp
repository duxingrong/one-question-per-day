/*
51.N皇后
*/
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

/**
 * @brief A solution to the N-Queens problem
 *
 * This class solves the N-Queens problem using backtracking
 */
class Solution {
public:
  /**
   * @brief 返回所有N皇后的情况
   *
   * @param n 皇后的数量
   * @return A vector of vector of strings
   */
  vector<vector<string>> solveNQueens(int n) {
    vector<string> board(n, string(n, '.'));
    backtracking(0, n, board);
    return result;
  }

private:
  set<int> backdiagonals;
  set<int> diagonals;
  set<int> cols;
  vector<vector<string>> result;
  /**
   * @ brief 回溯算法
   *
   * @param row 深搜到了第几层
   * @param n 总层
   * @param board 棋盘
   */

  void backtracking(int row, int n, vector<string> &board) {
    if (row == n) {
      result.push_back(board);
      return;
    }

    for (int col = 0; col < n; ++col) {
      int diagonal = row - col;
      int backdiagonal = row + col;
      if (cols.find(col) != cols.end() ||
          diagonals.find(diagonal) != diagonals.end() ||
          backdiagonals.find(backdiagonal) != backdiagonals.end()) {
        continue;
      } else {
        board[row][col] = 'Q';
        cols.insert(col);
        diagonals.insert(diagonal);
        backdiagonals.insert(backdiagonal);
        backtracking(row + 1, n, board);
        board[row][col] = '.';
        cols.erase(col);
        diagonals.erase(diagonal);
        backdiagonals.erase(backdiagonal);
      }
    }
  }
};

int main() {
  Solution obj;
  vector<vector<string>> result = obj.solveNQueens(4);
  for (const auto &tmp : result) {
    for (const auto &tmp2 : tmp) {
      cout << tmp2 << endl;
    }
    cout << endl;
  }
}
