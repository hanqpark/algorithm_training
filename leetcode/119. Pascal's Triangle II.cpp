/**
 * @file 119. Pascal's Triangle II.cpp
 * @author hanqpark
 * @link https://leetcode.com/problems/pascals-triangle-ii/
 * @version 0.1
 * @date 2025-02-18
 * 
 * @copyright Copyright (c) 2025
 * 
 */

#include <vector>
#include <iostream>

using namespace std;

vector<int> getRow(int rowIndex) {
    if (rowIndex == 0) return {1};
    
    vector<int> answer = {1, 1};
    for (int i = 1; i < rowIndex; ++i) {
        vector<int> temp = {1};
        for (int j = 0; j < i; ++j) {
            temp.push_back(answer[j] + answer[j+1]);
        }
        temp.push_back(1);
        answer = temp;
    }
    return answer;
}

vector<int> bestAnswer(int rowIndex) {
    vector<int> answer(rowIndex + 1, 1);
    
    for (int i = 1; i < rowIndex; ++i) {
        for (int j = i; j > 0; --j) { 
            answer[j] += answer[j - 1];
        }
    }
    
    return answer;
}

int main() {
    // auto answer = getRow(5);
    auto answer = bestAnswer(5);
    for (auto a: answer)
        cout << a << ", ";
    cout << endl;

    return 0;
}