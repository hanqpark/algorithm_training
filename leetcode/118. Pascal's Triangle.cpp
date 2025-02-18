/**
 * @file 118. Pascal's Triangle.cpp
 * @author hanqpark
 * @link  https://leetcode.com/problems/pascals-triangle/description/
 * @version 0.1
 * @date 2025-02-18
 */

#include <vector>
#include <iostream>

using namespace std;

vector<vector<int>> generate(int numRows) {
    vector<vector<int>> answer = {{1}, {1, 1}};
    if (numRows == 1) {
        return {{1}};
    } 

    for (int i = 2; i < numRows; ++i) {
        vector<int> temp = {1};
        for (int j = 0; j < i-1; ++j) {
            int sum = answer[i-1][j] + answer[i-1][j+1];
            temp.push_back(sum);
        }
        temp.push_back(1);
        answer.push_back(temp);
    }
    return answer;
}

int main() {
    auto answer = generate(5);
    for (auto a: answer) {
        for (auto b: a) {
            cout << b << ", ";
        }
        cout << endl;
    }
}