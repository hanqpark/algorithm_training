/**
 * @file 같은 숫자는 싫어.cpp
 * @author hanqpark
 * @link https://school.programmers.co.kr/learn/courses/30/lessons/12906 
 * @date 2025-04-06
 */

#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    
    for (const int& i: arr) {
        if (answer.size() == 0 || answer.back() != i) {
            answer.emplace_back(i);
        }
    }
    
    return answer;
}