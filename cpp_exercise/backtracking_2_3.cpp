#include <iostream>
#include <set>
#include <vector>
using namespace std;

/**
 * @brief 解数独，也就是填满9*9的格子，保证row,col,以及3*3的小格子中没有重复数字
 */
class Solution {
public:
  /**
   * @brief 主函数，主要是创建集合并且初始化
   *
   * @param board 9*9的棋盘
   *
   * @return None 直接在board上修改
   */
  void solveSudoku(vector<vector<char>> &board) {
    vector<set<char>> col_used(9);
    vector<set<char>> row_used(9);
    vector<set<char>> box_used(9);

    for (size_t row = 0; row < 9; ++row) {
      for (size_t col = 0; col < 9; ++col) {
        char num = board[row][col];
        if (num == '.')
          continue;
        row_used[row].insert(num);
        col_used[col].insert(num);
        box_used[(row / 3) * 3 + col / 3].insert(
            num); //只要 row 和 col 是整数类型（如 int），那么就自动是整除运算
      }
    }
    backtracking(0, 0, row_used, col_used, box_used, board);
  }

private:
  /**
   * @brief 利用递归回溯来依次处理所有的位置
   *
   * @param row 行
   * @param col 列
   * @param row_used 每一行的去重集合
   * @param col_used 每一列的去重集合
   * @param box_used 每一个3*3格子的去重集合
   * @param board 棋盘
   */
  bool backtracking(int row, int col, vector<set<char>> &row_used,
                    vector<set<char>> &col_used, vector<set<char>> &box_used,
                    vector<vector<char>> &board) {
    if (row == 9) {
      return true;
    }
    int next_row = (col < 8) ? row : row + 1;
    int next_col = (col < 8) ? col + 1 : 0;
    if (board[row][col] != '.') {
      return backtracking(next_row, next_col, row_used, col_used, box_used,
                          board);
    } else {
      for (char num = '1'; num <= '9'; ++num) {
        if (row_used[row].find(num) != row_used[row].end() ||
            col_used[col].find(num) != col_used[col].end() ||
            box_used[(row / 3) * 3 + col / 3].find(num) !=
                box_used[(row / 3) * 3 + col / 3].end()) {
          continue;
        } else {
          board[row][col] = num;
          row_used[row].insert(num);
          col_used[col].insert(num);
          box_used[(row / 3) * 3 + col / 3].insert(num);
          if (backtracking(next_row, next_col, row_used, col_used, box_used,
                           board)) {
            return true;
          }
          board[row][col] = '.';
          row_used[row].erase(num);
          col_used[col].erase(num);
          box_used[(row / 3) * 3 + col / 3].erase(num);
        }
      }
      return false;
    }
  }
};

int main() {
  vector<vector<char>> board = {{'5', '3', '.', '.', '7', '.', '.', '.', '.'},
                                {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
                                {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
                                {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
                                {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
                                {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
                                {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
                                {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
                                {'.', '.', '.', '.', '8', '.', '.', '7', '9'}};

  Solution s;
  s.solveSudoku(board);

  // 打印结果
  for (auto &row : board) {
    for (auto &c : row) {
      cout << c << ' ';
    }
    cout << '\n';
  }

  return 0;
}
