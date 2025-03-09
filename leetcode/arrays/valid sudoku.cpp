/**
 * @file valid sudoku.cpp
 * @author hanqpark
 * @link https://neetcode.io/problems/valid-sudoku
 * @date 2025-03-09
 */

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool myValidSudoku(vector<vector<char>>& board) {
        for (int i = 0; i < 9; ++i) {
            vector<int> col(9, 0);
            vector<int> row(9, 0);
            for (int j = 0; j < 9;  ++j) {
                char ch = board[i][j];
                if (ch != '.') {
                    int idx = ch - '0';
                    if (col[idx-1] == 0) {
                        col[idx-1]++;
                    } else {
                        return false;
                    }
                }
                ch = board[j][i];
                if (ch != '.') {
                    int idx = ch - '0';
                    if (row[idx-1] == 0) {
                        row[idx-1]++;
                    } else {
                        return false;
                    }
                }
            }
        }
        for (int i = 0; i < 9; i += 3) {
            for (int j = 0; j < 9; j += 3) {
                vector<int> box(9, 0);
                for (int x = 0; x < 3; ++x) {
                    for (int y = 0; y < 3; ++y) {
                        char ch = board[i+x][j+y];
                        if (ch != '.') {
                            int idx = ch - '0';
                            if (box[idx-1] == 0) {
                                box[idx-1]++;
                            } else {
                                return false;
                            }
                        }
                    }
                }
            }
        }
        return true;
    }

    bool bestValidSudoku(vector<vector<char>>& board) {
        vector<vector<bool>> row(9, vector<bool>(9, false));
        vector<vector<bool>> col(9, vector<bool>(9, false));
        vector<vector<bool>> box(9, vector<bool>(9, false));

        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] == '.') continue;

                int num = board[i][j] - '1'; // 0~8로 변환
                int boxIdx = (i / 3) * 3 + (j / 3); // 3×3 박스 인덱스 계산

                if (row[i][num] || col[j][num] || box[boxIdx][num]) {
                    return false;
                }

                row[i][num] = col[j][num] = box[boxIdx][num] = true;
            }
        }

        return true;
    }
};

int main() {
    Solution sol;
    vector<vector<char>> board = {
        {'1','2','.','.','3','.','.','.','.'},
        {'4','.','.','5','.','.','.','.','.'},
        {'.','9','8','.','.','.','.','.','3'},
        {'5','.','.','.','6','.','.','.','4'},
        {'.','.','.','8','.','3','.','.','5'},
        {'7','.','.','.','2','.','.','.','6'},
        {'.','.','.','.','.','.','2','.','.'},
        {'.','.','.','4','1','9','.','.','8'},
        {'.','.','.','.','8','.','.','7','9'}
    };

    cout << (sol.bestValidSudoku(board) ? "Valid Sudoku" : "Invalid Sudoku") << endl;

    return 0;
}